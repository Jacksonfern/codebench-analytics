import logging
import re
from os import path
from typing import List, Optional

from codebench_analytics.extractor import Extractor
from codebench_analytics.model.codebench_types import QuestionExecution, Resource
from codebench_analytics.utils.assessments_filter import (
    AssessmentFilter,
    AssessmentType,
)
from codebench_analytics.utils.code_diff import code_diff
from codebench_analytics.utils.components import Components
from codebench_analytics.utils.dataset import save

logger = logging.getLogger(__name__)


class ExecutionExtractor(Extractor):
    """Extract data about student executions."""

    TERMINATOR = "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

    def extract_from(self, kinds: Optional[list[AssessmentType]] = None) -> str:
        data: List[dict] = []
        for src in self.dataset_src:
            logger.info("extracting execution data from '%s'", src)
            partial_data = self._collect(src, kinds)
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

    def _collect(
        self, dataset_src: str, kinds: Optional[list[AssessmentType]]
    ) -> list:
        execs = Components.get_users_data(dataset_src, self.resource)
        assessments_filtered = AssessmentFilter.get(dataset_src, kinds)
        year = path.basename(dataset_src)
        log_rows = []

        for key, values in execs.items():
            class_, student = key.split("-", 1)
            for src in values:
                name = path.basename(src).split(".")[0]
                assessment_id, question_id = name.split("_", 1)
                assessment_id, question_id = int(assessment_id), int(question_id)

                if assessment_id not in assessments_filtered:
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
                        ln = lines[i].strip()
                        if ln.startswith("== SUBMITION"):
                            row["execution_type"] = "submission"
                            op = QuestionExecution.SUBMIT
                        elif ln.startswith("== TEST"):
                            row["execution_type"] = "test"
                            op = QuestionExecution.TEST
                        elif ln.startswith("-- ERROR:"):
                            assert (
                                op != QuestionExecution.NONE
                            ), "no submission or test for execution error"
                            row["run"] = "error"
                            while i < len(lines):
                                error_line = lines[i].strip()
                                error_type = re.fullmatch(
                                    r"(.*)Error:.*", error_line
                                )
                                if error_type:
                                    row["run_error_type"] = error_type.groups()[
                                        0
                                    ].lower()
                                    op = QuestionExecution.NONE
                                    break
                                elif error_line == self.TERMINATOR:
                                    row["run_error_type"] = "unknown"
                                    break
                                i += 1
                        elif ln.startswith("-- GRADE:"):
                            i += 1
                            grade = lines[i].strip()

                            assert (
                                op == QuestionExecution.SUBMIT
                            ), f"Response for non submission in {fullpath}"
                            assert re.match(r"\d+\%", grade), "Not a percent number"

                            row["run"] = "successful"
                            row["grade"] = grade[:-1]
                        elif ln.startswith("-- CODE:"):
                            while i + 1 < len(lines):
                                next_line = lines[i + 1].strip()
                                if (
                                    next_line.startswith("--")
                                    or next_line == self.TERMINATOR
                                ):
                                    break
                                cur_code.append(next_line)
                                i += 1
                            assert (
                                len(cur_code) > 0
                            ), "empty code submitted/tested on {}".format(
                                {**base_row, **row}
                            )

                            if len(prev_code) > 0:
                                row["amount_of_change"] = code_diff(
                                    prev_code, cur_code
                                )
                            prev_code = cur_code
                            cur_code = []
                        elif ln.startswith("-- OUTPUT:"):
                            row["run"] = "successful"

                        if ln == self.TERMINATOR:
                            log_rows.append({**base_row, **row})
                            row = {}
                        i += 1
        return log_rows


if __name__ == "__main__":
    ExecutionExtractor(
        "/home/jackson/Downloads/2023-1", resource=Resource.EXECUTIONS
    ).extract_from([AssessmentType.EXAM])
