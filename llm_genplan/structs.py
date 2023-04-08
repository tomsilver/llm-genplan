"""Data structures."""

import importlib.util
import logging
import sys
import tempfile
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import List, Set, Tuple, Union

from pyperplan.grounding import ground as pyperplan_ground
from pyperplan.pddl.parser import Parser
from pyperplan.pddl.pddl import Domain as PyperplanDomain
from pyperplan.pddl.pddl import Predicate as PyperplanPredicate
from pyperplan.pddl.pddl import Problem as PyperplanProblem
from pyperplan.pddl.pddl import Type as PyperplanType
from pyperplan.task import Operator as PyperplanOperator
from pyperplan.task import Task as PyperplanTask

PyperplanObject = str

__all__ = [
    "PyperplanDomain",
    "PyperplanPredicate",
    "PyperplanProblem",
    "PyperplanType",
    "PyperplanOperator",
    "PyperplanTask",
]


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
    def _parser(self) -> Parser:
        return Parser(self.domain_file, self.problem_file)

    @cached_property
    def domain(self) -> PyperplanDomain:
        """The parsed PDDL domain for this task."""
        return self._parser.parse_domain()

    @cached_property
    def typed(self) -> bool:
        """Whether the domain is typed."""
        return set(self.domain.types) != {"object"}

    @cached_property
    def problem(self) -> PyperplanProblem:
        """The parsed PDDL problem for this task."""
        return self._parser.parse_problem(self.domain)

    @cached_property
    def size(self) -> int:
        """A crude measure of task complexity."""
        prob = self.problem
        return len(prob.objects) + len(prob.initial_state) + len(prob.goal)

    @cached_property
    def pyperplan_task(self) -> PyperplanTask:
        """The pyperplan task for this task."""
        logging.disable(logging.ERROR)
        pyperplan_task = pyperplan_ground(
            self.problem,
            remove_irrelevant_operators=False,
            remove_statics_from_initial_state=False,
            remove_statics_from_operators=False,
        )
        logging.disable(logging.NOTSET)
        return pyperplan_task

    @cached_property
    def objects(self) -> Union[Set[Tuple[str, str]], Set[str]]:
        """The objects (not including constants) and their types."""
        objs = set()
        for obj in self.problem.objects:
            if self.typed:
                obj_type = self.problem.objects[obj]
                objs.add((obj, str(obj_type)))
            else:
                objs.add(obj)
        return objs

    @cached_property
    def init(self) -> Set[Tuple[str, ...]]:
        """The initial atoms in the form {(predicate name, object names)}."""
        return {pred_to_tuple(p) for p in self.problem.initial_state}

    @cached_property
    def goal(self) -> Set[Tuple[str, ...]]:
        """The goal in the form {(predicate name, object names)}."""
        return {pred_to_tuple(p) for p in self.problem.goal}

    @cached_property
    def actions_hint(self) -> str:
        """Write the action signatures."""
        signatures: List[str] = []
        for op_name in sorted(self.domain.actions):
            var_names = [v for v, _ in self.domain.actions[op_name].signature]
            if not var_names:
                signature = f"({op_name})"
            else:
                arg_names = " ".join(var_names)
                signature = f"({op_name} {arg_names})"
            signatures.append(signature)
        return " ".join(signatures)


@dataclass(frozen=True)
class GeneralizedPlan:
    """Wrapper around a generalized plan code string.

    The code should should be of the form

    def get_plan(task):
        # Your code here
        return plan

    where
        - `task.objects` is a set of (object name, object type name) tuples
           if the domain is typed, and just object name strings otherwise
        - `task.init` is a set of ground atoms represented as tuples of predicate
           names and arguments (e.g., ('predicate-foo', 'object-bar', ...))
        - `task.goal` is also a set of ground atoms represented in the same way
        - `plan` is a list of actions, where each action is a ground operator
           represented as a string (e.g., '(operator-baz object-qux ...)').
    """

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
        return module.get_plan(task)  # type: ignore  # pylint: disable=undefined-variable


def pred_to_tuple(pred: PyperplanPredicate) -> Tuple[str, ...]:
    """Create a tuple representation of a Pyperplan predicate (atom)."""
    arg_strs = [str(o) for o, _ in pred.signature]
    return (pred.name,) + tuple(arg_strs)
