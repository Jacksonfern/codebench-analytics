from typing import Dict, List, Tuple
import csv
from codebench_analytics.metrics import Collector, QuestionMetrics, StudentQuestionInfo

from codebench_analytics.utils import save


class ExecutionCollector(Collector):
    """
    This class extracts metrics related to students code submissions
    on codebench and generate statistics for each question.
    The basic metrics extracted here is:

    Attributes
    ----------
    TODO:
    """

    @staticmethod
    def collect(csv_source: str) -> None:
        students_info: Dict[Tuple[int, int], StudentQuestionInfo] = {}
        with open(csv_source, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                for row in reader:
                    row_question = int(row["question"])
                    row_student = int(row["student"])
                    key = (row_student, row_question)

                    if not key in students_info:
                        students_info[key] = StudentQuestionInfo()

                    question = students_info[key]
                    if question.is_correct:
                        continue

                    row_exec_type = row["execution_type"]
                    if row_exec_type == "submission":
                        question.num_submissions += 1
                        if row["run"] == "successful":
                            if int(row["grade"]) == 100:
                                question.is_correct = True
                            else:
                                question.num_errors += 1
                                question.num_logic_errors += 1
                        else:
                            question.num_errors += 1
                            # if row['run_error_type'] == 'syntax':
                            question.num_syntax_errors += 1
                    elif row_exec_type == "test":
                        question.num_tests += 1

                    if row["amount_of_change"]:
                        question.amount_of_change += int(row["amount_of_change"])
            except csv.Error:
                print("error processing csv file on line {}".format(reader.line_num))

        store_data: List[dict] = []
        csv_fields = ["student", "question", *vars(StudentQuestionInfo()).keys()]
        for key, info in students_info.items():
            if info.num_submissions > 0:
                student, question = key
                store_data.append(
                    {"student": student, "question": question, **vars(info)}
                )
        save("output/metrics", "executions_by_student.csv", store_data, csv_fields)

        questions_statistics: Dict[int, QuestionMetrics] = {}
        for key, info in students_info.items():
            _, question = key
            if not question in questions_statistics:
                questions_statistics[question] = QuestionMetrics()
            qs = questions_statistics[question]

            # TODO: check if this is the correct filter
            if info.num_submissions == 0:
                continue

            qs.num_students_interactions += 1
            if info.is_correct:
                qs.num_correct += 1

            qs.num_submissions += info.num_submissions
            qs.num_errors += info.num_errors
            qs.num_logic_errors += info.num_logic_errors
            qs.num_tests += info.num_tests
            qs.num_syntax_errors += info.num_syntax_errors
            qs.amount_of_change += info.amount_of_change

            assert (
                qs.num_errors >= qs.num_logic_errors
            ), "the number of logic errors is bigger than the number of all possible errors"

        toErase = filter(
            lambda id: questions_statistics[id].num_students_interactions == 0,
            questions_statistics,
        )
        for id in list(toErase):
            questions_statistics.pop(id)

        csv_fields = list(vars(QuestionMetrics()).keys())
        save(
            "output/metrics",
            "executions.csv",
            questions_statistics,
            ["question", *csv_fields],
        )
