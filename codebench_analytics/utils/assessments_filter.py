from enum import StrEnum, auto
from os import path

from codebench_analytics.model.codebench_types import Data
from codebench_analytics.utils.components import Components
import logging


class AssessmentType(StrEnum):
    EXAM = auto()
    HOMEWORK = auto()


class AssessmentFilter:
    """Filter assessments by set of kinds.

    If no kind is set, it will get all. See the `AssessmentType` to see
    all possible kinds.
    """

    @staticmethod
    def get(dataset_src, kinds: list[AssessmentType] = None):
        """Get all the assessments from given kinds, such as homeworks and exams."""

        assessments = Components.get_data(dataset_src, Data.ASSESSMENT)
        assessment_ids = []

        for assessment in assessments:
            filename = path.basename(assessment)
            fullpath = path.join(dataset_src, assessment)
            assessment_id = filename.split(".")[0]
            with open(fullpath, "r") as file:
                for line in file:
                    # each assessment has a line identifying its type
                    # e.g. `---- type: homework`
                    if line.startswith("---- type:"):
                        kind = AssessmentType(line.split(":")[-1].strip())
                        if not kinds or kind in kinds:
                            assessment_ids.append(int(assessment_id))
                            break

        return assessment_ids


# Only for testing purposes
if __name__ == "__main__":
    d = AssessmentFilter.get(
        "/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2017-1"
    )
    print(d)
