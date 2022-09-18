from abc import abstractmethod
from enum import Enum
from typing import List

class Collector:
    @abstractmethod
    def collect(csv_source: str):
        pass

class Metric:
    def __init__(self, *dataset_src, resource: Enum):
        self.dataset_src = dataset_src
        self.resource = resource

    @abstractmethod
    def collect(self, kinds=List[str]) -> str:
        pass

class QuestionMetrics:
    """
    Retrieves students executions and store metrics related to questions.
    
    Note
    ----
    When a question is solved by a student, all executions 
    after that will not be considered

    Attributes
    ----------
    TODO
    """

    def __init__(self, num_students_interactions = 0, num_submissions = 0, num_tests = 0, num_correct = 0, 
                num_errors = 0, num_logic_errors = 0, num_syntax_errors = 0, amount_of_change = 0):
        self.num_students_interactions = num_students_interactions
        self.num_submissions = num_submissions
        self.num_tests = num_tests

        self.num_correct = num_correct
        self.num_errors = num_errors
        self.num_logic_errors = num_logic_errors
        self.num_syntax_errors = num_syntax_errors
        self.amount_of_change = amount_of_change

    def __add__(self, other):
        return QuestionMetrics(
            self.num_students_interactions + other.num_students_interactions,
            self.num_submissions + other.num_submissions,
            self.num_tests + other.num_tests,
            self.num_correct + other.num_correct,
            self.num_errors + other.num_errors,
            self.num_logic_errors + other.num_logic_errors,
            self.num_syntax_errors + other.num_syntax_errors,
            self.amount_of_change + other.amount_of_change
        )

class StudentQuestionInfo:
    def __init__(self, is_correct = False, num_submissions = 0, num_tests = 0, 
                num_errors = 0, num_logic_errors = 0, num_syntax_errors = 0, amount_of_change = 0):
        self.is_correct = is_correct
        self.num_submissions = num_submissions
        self.num_tests = num_tests
        self.num_errors = num_errors
        self.num_logic_errors = num_logic_errors
        self.num_syntax_errors = num_syntax_errors
        self.amount_of_change = amount_of_change

class StudentCodeInfo:
    def __init__(self, is_correct = False, submitted = False, code_time = 0, num_events = 0, num_deletes = 0, last_time = None) -> None:
        self.is_correct = is_correct
        self.submitted = submitted
        self.code_time = code_time
        self.num_events = num_events
        self.num_deletes = num_deletes
        self.last_time = last_time

class CodeMetrics:
    def __init__(self, code_time = 0, num_events = 0, num_deletes = 0, num_blank = 0) -> None:
        self.code_time = code_time
        self.num_events = num_events
        self.num_deletes = num_deletes
        self.num_blank = num_blank

class ActionInfo:
    def __init__(self, date, event_type, event_key = None, event_op = None) -> None:
        self.date = date
        self.event_type = event_type
        self.event_key = event_key
        self.event_op = event_op