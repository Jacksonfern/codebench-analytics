from abc import ABC, abstractmethod
from typing import Optional

from codebench_analytics.utils.assessments_filter import AssessmentType
from codebench_analytics.model.codebench_types import Resource


class Extractor(ABC):
    """Extract data from codebench logs."""

    def __init__(self, *dataset_src, resource: Resource):
        self.dataset_src = dataset_src
        self.resource = resource

    @abstractmethod
    def extract_from(self, kinds: Optional[list[AssessmentType]] = None) -> str:
        pass
