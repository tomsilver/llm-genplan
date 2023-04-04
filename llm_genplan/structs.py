"""Data structures."""

import logging
import tempfile
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import List, Set, Tuple

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
        )
        logging.disable(logging.NOTSET)
        return pyperplan_task

    @cached_property
    def objects(self) -> Set[Tuple[str, str]]:
        """The objects (not including constants) and their types."""
        objs = set()
        for obj in sorted(self.problem.objects):
            obj_type = self.problem.objects[obj]
            objs.add((obj, str(obj_type)))
        return objs

    @cached_property
    def init(self) -> Set[Tuple[str, ...]]:
        """The initial atoms in the form {(predicate name, object names)}."""
        return {pred_to_tuple(p) for p in self.problem.initial_state}

    @cached_property
    def goal(self) -> Set[Tuple[str, ...]]:
        """The goal in the form {(predicate name, object names)}."""
        return {pred_to_tuple(p) for p in self.problem.goal}

    def goal_holds(self) -> bool:
        """Check if the goal holds in the initial state."""
        return self.goal.issubset(self.init)

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

    def get_plan(objects, init, goal):
        # Your code here
        return plan

    where
        - `objects` is a set of (object name, object type name) tuples
           if the domain is typed, and just object name strings otherwise
        - `init` is a set of ground atoms represented as tuples of predicate
           names and arguments (e.g., ('predicate-foo', 'object-bar', ...))
        - `goal` is also a set of ground atoms represented in the same way
        - `plan` is a list of actions, where each action is represented as a
           tuple of operator name and arguments (e.g., ('operator-baz',
           'object-qux', ...)).
    """

    code_str: str

    def run(self, task: Task) -> List[str]:
        """Run the generalized plan to get a plan for the task."""
        # Add get_plan() to globals().
        exec(self.code_str, globals())  # pylint: disable=exec-used
        # Run the generalized plan.
        if task.typed:
            objects = task.objects
        else:
            objects = {o for o, _ in task.objects}  # type: ignore
        action_tuples = get_plan(objects, task.init, task.goal)  # type: ignore  # pylint: disable=undefined-variable
        # Convert to string representation.
        return [action_tuple_to_action(a) for a in action_tuples]


def pred_to_tuple(pred: PyperplanPredicate) -> Tuple[str, ...]:
    """Create a tuple representation of a Pyperplan predicate (atom)."""
    arg_strs = [str(o) for o, _ in pred.signature]
    return (pred.name,) + tuple(arg_strs)


def action_tuple_to_action(act_tuple: Tuple[str, ...]) -> str:
    """Create a string action from a tuple."""
    op_name = act_tuple[0]
    if len(act_tuple) == 1:
        return f"({op_name})"
    arg_names = act_tuple[1:]
    arg_name_str = " ".join(arg_names)
    return f"({op_name} {arg_name_str})"
