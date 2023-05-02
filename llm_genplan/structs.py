"""Data structures."""

import tempfile
from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, Set, Tuple, Union

from pddlgym.parser import Literal, PDDLDomainParser, PDDLProblemParser


@dataclass(frozen=True)
class Task:
    """A task is a PDDL domain str and problem str."""

    domain_str: str
    problem_str: str

    @cached_property
    def domain_file(self) -> Path:
        """A file that contains the domain str."""
        filename = tempfile.NamedTemporaryFile(delete=False).name
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.domain_str)
        return Path(filename)

    @cached_property
    def problem_file(self) -> Path:
        """A file that contains the problem str."""
        filename = tempfile.NamedTemporaryFile(delete=False).name
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.problem_str)
        return Path(filename)

    @cached_property
    def domain(self) -> PDDLDomainParser:
        """The parsed PDDL domain."""
        return PDDLDomainParser(
            self.domain_file, expect_action_preds=False, operators_as_actions=True
        )

    @cached_property
    def problem(self) -> PDDLProblemParser:
        """The parsed PDDL problem."""
        return PDDLProblemParser(
            self.problem_file,
            self.domain.domain_name,
            self.domain.types,
            self.domain.predicates,
            self.domain.actions,
            self.domain.constants,
        )

    @cached_property
    def typed(self) -> bool:
        """Whether the domain is typed."""
        return self.domain.uses_typing

    @property
    def objects(self) -> Union[Set[Tuple[str, str]], Set[str]]:
        """The objects (not including constants) and their types."""
        if not self.typed:
            return {o.name for o in self.problem.objects}
        return {(o.name, str(o.var_type)) for o in self.problem.objects}

    @property
    def init(self) -> Set[Tuple[str, ...]]:
        """The initial atoms in string form."""
        return {_literal_to_tuple(l) for l in self.problem.initial_state}

    @property
    def goal(self) -> Set[Tuple[str, ...]]:
        """The goal in string form."""
        return {_literal_to_tuple(l) for l in self.problem.goal.literals}

    @cached_property
    def size(self) -> int:
        """Crude estimate of task size."""
        return len(self.objects) + len(self.init) + len(self.goal)

    @cached_property
    def problem_name(self) -> str:
        """The problem name."""
        key = "(problem "
        s = self.problem_str.index(key)
        e = self.problem_str[s:].index(")")
        return self.problem_str[s + len(key) : s + e]

    @cached_property
    def domain_name(self) -> str:
        """The domain name."""
        key = "(domain "
        s = self.domain_str.index(key)
        e = self.domain_str[s:].index(")")
        return self.domain_str[s + len(key) : s + e]

    def get_abbreviated_problem_str(
        self,
        max_objects_per_type: int = 10,
        max_init_atoms_per_type: int = 10,
        max_goal_atoms_per_type: int = 10,
    ) -> str:
        """A shortened version of the problem string."""
        # Build objects.
        object_type_to_strs: DefaultDict[str, List[str]] = defaultdict(list)
        for obj in sorted(self.objects):
            if self.typed:
                assert isinstance(obj, tuple)
                obj_name, obj_type = obj
                obj_str = f"{obj_name} - {obj_type}"
            else:
                assert isinstance(obj, str)
                obj_type = "default"
                obj_str = obj
            object_type_to_strs[obj_type].append(obj_str)
        # Abbreviate.
        object_strs: List[str] = []
        for obj_type in sorted(object_type_to_strs):
            type_obj_strs = object_type_to_strs[obj_type]
            if len(type_obj_strs) > max_objects_per_type:
                type_obj_strs = type_obj_strs[:max_objects_per_type]
                type_obj_strs.append("...")
            object_strs.extend(type_obj_strs)
        objects_str = "\n    ".join(object_strs)
        # Build init.
        pred_to_init_strs: DefaultDict[str, List[str]] = defaultdict(list)
        for atom_tuple in sorted(self.init):
            pred = atom_tuple[0]
            atom_str = "(" + " ".join(atom_tuple) + ")"
            pred_to_init_strs[pred].append(atom_str)
        # Abbreviate.
        init_strs: List[str] = []
        for pred in sorted(pred_to_init_strs):
            pred_strs = pred_to_init_strs[pred]
            if len(pred_strs) > max_init_atoms_per_type:
                pred_strs = pred_strs[:max_init_atoms_per_type]
                pred_strs.append("...")
            init_strs.extend(pred_strs)
        init_str = "\n    ".join(init_strs)
        # Build goal.
        pred_to_goal_strs: DefaultDict[str, List[str]] = defaultdict(list)
        for atom_tuple in sorted(self.goal):
            pred = atom_tuple[0]
            atom_str = "(" + " ".join(atom_tuple) + ")"
            pred_to_goal_strs[pred].append(atom_str)
        # Abbreviate.
        goal_strs: List[str] = []
        for pred in sorted(pred_to_goal_strs):
            pred_strs = pred_to_goal_strs[pred]
            if len(pred_strs) > max_goal_atoms_per_type:
                pred_strs = pred_strs[:max_goal_atoms_per_type]
                pred_strs.append("...")
            goal_strs.extend(pred_strs)
        goal_str = "\n    ".join(goal_strs)

        return f"""(define (problem {self.problem_name} (:domain {self.domain_name})
  (:objects
    {objects_str}
  )
  (:init
    {init_str}
  )
  (:goal (and
    {goal_str}
    )
  )    
)
        """

    def action_has_valid_syntax(self, action: Any) -> bool:
        """Check if the action name and arity is correct and objects exist."""
        if not isinstance(action, str):
            return False
        if not (action.startswith("(") and action.endswith(")")):
            return False
        action = action[1:-1].strip()
        if " " not in action:
            name = action
            arg_names = []
        else:
            name, remainder = action.split(" ", 1)
            arg_names = remainder.split(" ")
        if name not in self.domain.operators:
            return False
        if len(arg_names) != len(self.domain.operators[name].params):
            return False
        return True

    @cached_property
    def actions_hint(self) -> str:
        """Write the action signatures."""
        act_strs: List[str] = []
        for act_name in sorted(self.domain.operators):
            op = self.domain.operators[act_name]
            param_str = " ".join(p.name for p in op.params)
            act_str = f"({act_name} {param_str})"
            act_strs.append(act_str)
        return " ".join(act_strs)


def _literal_to_tuple(lit: Literal) -> Tuple[str, ...]:
    arg_strs = [v.name for v in lit.variables]
    return (lit.predicate.name,) + tuple(arg_strs)


Metrics = Dict[str, Any]
