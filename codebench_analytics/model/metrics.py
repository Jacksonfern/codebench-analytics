from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class QuestionMetrics:
    """Retrieves students executions and store metrics related to questions.

    Note
    ----
    When a question is solved by a student, all executions
    after that will not be considered
    """

    num_students_interactions: int = 0
    num_submissions: int = 0
    num_tests: int = 0
    num_correct: int = 0
    num_errors: int = 0
    num_logic_errors: int = 0
    num_syntax_errors: int = 0
    amount_of_change: int = 0

    @property
    def to_dict(self):
        return {
            "num_students_interactions": self.num_students_interactions,
            "num_submissions": self.num_submissions,
            "num_tests": self.num_tests,
            "num_correct": self.num_correct,
            "num_errors": self.num_errors,
            "num_logic_errors": self.num_logic_errors,
            "num_syntax_errors": self.num_syntax_errors,
            "amount_of_change": self.amount_of_change,
        }

    def __add__(self, other):
        return QuestionMetrics(
            self.num_students_interactions + other.num_students_interactions,
            self.num_submissions + other.num_submissions,
            self.num_tests + other.num_tests,
            self.num_correct + other.num_correct,
            self.num_errors + other.num_errors,
            self.num_logic_errors + other.num_logic_errors,
            self.num_syntax_errors + other.num_syntax_errors,
            self.amount_of_change + other.amount_of_change,
        )


@dataclass(slots=True)
class StudentQuestionInfo:
    """Contains statistics about student solving a question."""

    is_correct: bool = False
    num_submissions: int = 0
    num_tests: int = 0
    num_errors: int = 0
    num_logic_errors: int = 0
    num_syntax_errors: int = 0
    amount_of_change: int = 0

    @property
    def to_dict(self):
        return {
            "is_correct": self.is_correct,
            "num_submissions": self.num_submissions,
            "num_tests": self.num_tests,
            "num_errors": self.num_errors,
            "num_logic_errors": self.num_logic_errors,
            "num_syntax_errors": self.num_syntax_errors,
            "amount_of_change": self.amount_of_change,
        }


@dataclass(slots=True)
class StudentCodeInfo:
    """Statistics about a code submitted by a student."""

    is_correct: bool = False
    submitted: bool = False
    code_time: int = 0
    num_events: int = 0
    num_deletes: int = 0
    last_time: Optional[int] = None

    @property
    def to_dict(self):
        return {
            "is_correct": self.is_correct,
            "submitted": self.submitted,
            "code_time": self.code_time,
            "num_events": self.num_events,
            "num_deletes": self.num_deletes,
            "last_time": self.last_time,
        }


@dataclass(slots=True)
class CodeMetrics:
    """General statistics about a question."""

    code_time: int = 0
    num_events: int = 0
    num_deletes: int = 0
    num_blank: int = 0

    @property
    def to_dict(self):
        return {
            "code_time": self.code_time,
            "num_events": self.num_events,
            "num_deletes": self.num_deletes,
            "num_blank": self.num_blank,
        }
