from logging.config import fileConfig
from typing import Optional

import click

from codebench_analytics.collector.actions import ActionCollector
from codebench_analytics.collector.executions import ExecutionCollector
from codebench_analytics.extractor.action_extractor import ActionsExtractor
from codebench_analytics.extractor.code_metrics_extractor import Solution
from codebench_analytics.extractor.execution_extractor import ExecutionExtractor
from codebench_analytics.model.code_metrics import SolutionMetrics
from codebench_analytics.model.codebench_types import Resource
from codebench_analytics.utils.assessments_filter import (
    AssessmentType,
)
from codebench_analytics.utils.dataset import save

fileConfig("codebench_analytics/logging/logging.ini")


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "-p",
    "--path",
    multiple=True,
    required=True,
    type=str,
    help="path to codebench dataset. It can be set multiple times",
)
@click.option("-k", "--kind", multiple=True, required=False, type=AssessmentType)
def execution(path: tuple[str], kind: Optional[tuple[AssessmentType]]):
    # transform codebench execution logs into csv datasets
    path = ExecutionExtractor(*path, resource=Resource.EXECUTIONS).extract_from(
        kinds=kind or None
    )
    # collect execution metrics from students
    ExecutionCollector(path).collect()


@click.command()
@click.option(
    "-p",
    "--path",
    multiple=True,
    required=True,
    type=str,
    help="path to codebench dataset. It can be set multiple times",
)
@click.option("-k", "--kind", multiple=True, required=False, type=AssessmentType)
def action(path: tuple[str], kind: Optional[tuple[AssessmentType]]):
    # transform codebench student actions logs into csv datasets
    path = ActionsExtractor(*path, resource=Resource.CODEMIRRORS).extract_from(
        kinds=kind or None
    )
    # collect action metrics from students
    ActionCollector(path).collect()


@click.command()
@click.option("-p", "--path", required=True, type=str, help="file with solutions")
def solution(path: str):
    res = Solution.extract_from_professor(path)
    csv_fields = list(vars(SolutionMetrics()).keys())
    save(
        "output/data",
        "code_metrics_professor.csv",
        res,
        ["question_id", *csv_fields],
    )


def main():
    cli.add_command(execution)
    cli.add_command(action)
    cli.add_command(solution)

    cli()


if __name__ == "__main__":
    main()
