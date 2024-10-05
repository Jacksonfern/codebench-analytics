from os import path
from typing import Dict

from cbTypes import QuestionStatus, QuestionExecution

from components import Components
from metrics import Metric, QuestionMetrics
from enum import Enum
from codebench_analytics.assessments_filter import AssessmentFilter
import re
from utils import save

class ExecutionMetrics(Metric):
    """
    This class extracts metrics related to students code submissions
    on codebench and generate statistics for each question. 
    The basic metrics extracted here is:

    Attributes
    ----------
    TODO:
    """

    def __init__(self, *dataset_src, resource: Enum):
        super().__init__(*dataset_src, resource=resource)

    def collect(self, kinds: list = None) -> None:
        statistics: Dict[str, QuestionMetrics] = {}
        for src in self.dataset_src:
            partial_statistics = self.__collect(src, kinds)
            for key, value in partial_statistics.items():
                if not key in statistics:
                    statistics[key] = value
                else:
                    statistics[key] += value

        # Erase questions with no user interaction (test or submission)
        toErase = filter(
            lambda id: statistics[id].num_submissions + statistics[id].num_tests == 0,
            statistics
        )
        for id in list(toErase):
            statistics.pop(id)  

        fields = vars(QuestionMetrics()).keys()
        csv_fields = ['question_id', *fields]

        save('executions.csv', statistics, csv_fields)


    def __collect(self, dataset_src: str, kinds: list = None) -> dict:
        print('Collecting {} from {}'.format(self.resource.value, dataset_src))
        execs = Components.getUsersData(dataset_src, self.resource)
        assessments_filtered = AssessmentFilter.get(dataset_src, kinds)
        question_statistics = {}

        for values in execs.values():
            for src in values:
                name = path.basename(src).split('.')[0]
                assessment_id, question_id = name.split('_', 1)
                assessment_id, question_id = int(assessment_id), int(question_id)

                if not assessment_id in assessments_filtered:
                    continue

                if not question_id in question_statistics:
                    question_statistics[question_id] = QuestionMetrics()

                fullpath = path.join(dataset_src, src)
                with open(fullpath, 'r') as log:
                    lines = log.readlines()
                    state = QuestionStatus.BLANK
                    op = QuestionExecution.NONE
                    metrics: QuestionMetrics = question_statistics[question_id]
                    i = 0

                    while i < len(lines):
                        l = lines[i].strip()
                        if l.startswith('== SUBMITION'):
                            op = QuestionExecution.SUBMIT
                            metrics.num_submissions += 1
                        elif l.startswith('== TEST'):
                            op = QuestionExecution.TEST
                            metrics.num_tests += 1
                        elif l.startswith('-- ERROR:'):
                            assert op != QuestionExecution.NONE, 'no submission or test for execution error'
                            if op == QuestionExecution.SUBMIT:
                                while i < len(lines):
                                    error_type = re.fullmatch(r"(\w*)Error:.*", lines[i].strip())
                                    if error_type:
                                        if error_type.groups()[0] == 'Syntax':
                                            metrics.num_syntax_errors += 1
                                            state = QuestionStatus.SYNTAX_ERROR
                                        else:
                                            metrics.num_errors_submissions += 1
                                            state = QuestionStatus.GENERAL_ERROR
                                        break
                                    i += 1
                            else:
                                metrics.num_errors_tests += 1
                        elif l.startswith('-- GRADE:'):
                            i += 1
                            grade = lines[i].strip()
                            assert op == QuestionExecution.SUBMIT, 'Response for non submission'
                            assert re.match(r"\d+\%", grade), 'Not a percent number'

                            if grade == '100%':
                                state = QuestionStatus.CORRECT
                                # Any submission/test after first corrected submission 
                                # are not taken into account.
                                break
                            else:
                                metrics.num_incorrect_submissions += 1
                                state = QuestionStatus.INCORRECT
                        i += 1

                    if state != QuestionStatus.BLANK:
                        metrics.num_students_interactions += 1
                    
                    if state == QuestionStatus.CORRECT:
                        metrics.num_correct += 1
                    elif state == QuestionStatus.INCORRECT:
                        metrics.num_incorrect += 1
                    elif state == QuestionStatus.SYNTAX_ERROR or state == QuestionStatus.GENERAL_ERROR:
                        metrics.num_errors += 1 
        
        return question_statistics