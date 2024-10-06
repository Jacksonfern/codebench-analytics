from logging.config import fileConfig

from collector.actions import ActionCollector
from collector.executions import ExecutionCollector
from extractor.execution_extractor import ExecutionExtractor

from codebench_analytics.extractor.action_extractor import ActionsExtractor
from codebench_analytics.extractor.code_metrics_extractor import Solution
from codebench_analytics.model.code_metrics import SolutionMetrics
from codebench_analytics.model.codebench_types import Resource
from codebench_analytics.utils.assessments_filter import (
    AssessmentType,
)
from codebench_analytics.utils.dataset import save

fileConfig("codebench_analytics/logging/logging.ini")


def main():
    srcs = ("/home/jackson/Downloads/2023-1",)
    kinds = [AssessmentType.EXAM]

    # transform codebench execution logs into csv datasets
    path = ExecutionExtractor(*srcs, resource=Resource.EXECUTIONS).extract_from(
        kinds=kinds
    )

    # collect execution metrics from students
    ExecutionCollector(path).collect()

    # transform codebench student actions logs into csv datasets
    path = ActionsExtractor(*srcs, resource=Resource.CODEMIRRORS).extract_from(
        kinds=kinds
    )

    # collect action metrics from students
    ActionCollector(path).collect()


def generate_code_metrics():
    src = "/home/jackson/Downloads/codigo_solucao.csv"
    res = Solution.extract_from_professor(src)
    csv_fields = list(vars(SolutionMetrics()).keys())
    save(
        "output/data",
        "code_metrics_professor.csv",
        res,
        ["question_id", *csv_fields],
    )


if __name__ == "__main__":
    main()
