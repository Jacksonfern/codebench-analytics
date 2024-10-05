from os import path
from typing import List
from codebench_analytics.cbTypes import QuestionExecution, Resource
from codebench_analytics.components import Components
from codebench_analytics.metrics import Metric
from enum import Enum
from codebench_analytics.assessments_filter import AssessmentFilter
from codebench_analytics.utils import save, codeDiff
import re


class ExecutionParser(Metric):
    """
    TODO:
    """

    def __init__(self, *dataset_src, resource: Enum):
        super().__init__(*dataset_src, resource=resource)

    def collect(self, kinds: list = None) -> str:
        data: List[dict] = []
        for src in self.dataset_src:
            partial_data = self.__collect(src, kinds)
            data.extend(partial_data)

        assert len(data) > 0, "empty dataset"

        csv_fields = [
            "semester",
            "class",
            "student",
            "assessment",
            "question",
            "execution_type",
            "run",
            "run_error_type",
            "grade",
            "amount_of_change",
        ]
        return save("output/data", "executions_data.csv", data, csv_fields)

    def __collect(self, dataset_src: str, kinds: list = None) -> list:
        print("Collecting {} from {}".format(self.resource.value, dataset_src))
        execs = Components.getUsersData(dataset_src, self.resource)
        assessments_filtered = AssessmentFilter.get(dataset_src, kinds)
        year = path.basename(dataset_src)
        log_rows = []

        for key, values in execs.items():
            class_, student = key.split("-", 1)
            for src in values:
                name = path.basename(src).split(".")[0]
                assessment_id, question_id = name.split("_", 1)
                assessment_id, question_id = int(assessment_id), int(question_id)

                if not assessment_id in assessments_filtered:
                    continue

                base_row = {
                    "semester": year,
                    "class": int(class_),
                    "student": int(student),
                    "assessment": assessment_id,
                    "question": question_id,
                }

                fullpath = path.join(dataset_src, src)
                with open(fullpath, "r") as log:
                    lines = log.readlines()
                    op = QuestionExecution.NONE
                    i = 0
                    row = {}
                    cur_code, prev_code = [], []

                    while i < len(lines):
                        l = lines[i].strip()
                        if l.startswith("== SUBMITION"):
                            row["execution_type"] = "submission"
                            op = QuestionExecution.SUBMIT
                        elif l.startswith("== TEST"):
                            row["execution_type"] = "test"
                            op = QuestionExecution.TEST
                        elif l.startswith("-- ERROR:"):
                            assert (
                                op != QuestionExecution.NONE
                            ), "no submission or test for execution error"
                            row["run"] = "error"
                            while i < len(lines):
                                l = lines[i].strip()
                                error_type = re.fullmatch(r"(.*)Error:.*", l)
                                if error_type:
                                    row["run_error_type"] = error_type.groups()[
                                        0
                                    ].lower()
                                    op = QuestionExecution.NONE
                                    break
                                elif (
                                    l
                                    == "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
                                ):
                                    row["run_error_type"] = "unknown"
                                    break
                                i += 1
                        elif l.startswith("-- GRADE:"):
                            i += 1
                            grade = lines[i].strip()

                            assert (
                                op == QuestionExecution.SUBMIT
                            ), f"Response for non submission {op} {fullpath}"
                            assert re.match(r"\d+\%", grade), "Not a percent number"

                            row["run"] = "successful"
                            row["grade"] = grade[:-1]
                        elif l.startswith("-- CODE:"):
                            while i + 1 < len(lines):
                                l = lines[i + 1].strip()
                                if l.startswith("--"):
                                    break
                                cur_code.append(l)
                                i += 1
                            assert (
                                len(cur_code) > 0
                            ), "empty code submitted/tested on {}".format(
                                {**base_row, **row}
                            )

                            if len(prev_code) > 0:
                                row["amount_of_change"] = codeDiff(prev_code, cur_code)
                            prev_code = cur_code
                            cur_code = []
                        elif l.startswith("-- OUTPUT:"):
                            row["run"] = "successful"

                        if l == "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*":
                            log_rows.append({**base_row, **row})
                            row = {}
                        i += 1
        return log_rows
