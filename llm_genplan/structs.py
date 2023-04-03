"""Data structures."""

import logging
import tempfile
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

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
        pyperplan_task = pyperplan_ground(self.problem)
        logging.disable(logging.NOTSET)
        return pyperplan_task


@dataclass(frozen=True)
class GeneralizedPlan:
    """Wrapper around a generalized plan code string.

    The code should should be of the form

    def get_plan(objects, init, goal):
        # Your code here
        return plan

    where
        - `objects` is a set of (object name, object type name) tuples
        - `init` is a set of ground atoms represented as tuples of predicate
           names and arguments (e.g., ('predicate-foo', 'object-bar', ...))
        - `goal` is also a set of ground atoms represented in the same way
        - `plan` is a list of actions, where each action is represented as a
           tuple of operator name and arguments (e.g., ('operator-baz',
           'object-qux', ...)).
    """

    code_str: str
