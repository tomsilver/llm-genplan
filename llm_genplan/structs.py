"""Data structures."""

import importlib.util
import sys
import tempfile
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import List, Set, Tuple, Union

from pddlgym.parser import PDDLDomainParser, PDDLProblemParser


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

    @cached_property
    def objects(self) -> Union[Set[Tuple[str, str]], Set[str]]:
        """The objects (not including constants) and their types."""
        return {o.name for o in self.problem.objects}

    @cached_property
    def init(self) -> Set[str]:
        """The initial atoms in string form."""
        return {l.pddl_str() for l in self.problem.initial_state}

    @cached_property
    def goal(self) -> Set[str]:
        """The goal in string form."""
        return {l.pddl_str() for l in self.problem.goal.literals}

    @cached_property
    def size(self) -> int:
        """Crude estimate of task size."""
        return len(self.objects) + len(self.init) + len(self.goal)

    def action_has_valid_syntax(self, action: str) -> bool:
        """Check if the action name and arity is correct and objects exist."""
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
        if not set(arg_names).issubset(self.objects):
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


@dataclass(frozen=True)
class GeneralizedPlan:
    """Wrapper around a generalized plan code string."""

    code_str: str

    @cached_property
    def filepath(self) -> Path:
        """Get a file with the code string implemented in it."""
        filename = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".py").name)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.code_str)
        return filename

    def run(self, task: Task) -> List[str]:
        """Run the generalized plan to get a plan for the task."""
        # Import get_plan().
        module_name = f"{self.filepath.stem}"
        spec = importlib.util.spec_from_file_location(module_name, self.filepath)
        assert spec is not None
        assert spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        assert module is not None
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        # Run the generalized plan.
        return module.get_plan(task.objects, task.init, task.goal)  # type: ignore  # pylint: disable=undefined-variable
