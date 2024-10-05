# ***********************USELESS FOR NOW*************************************

from typing import Dict, List, Optional

from codebench_analytics.extractor import Extractor
from codebench_analytics.model.metrics import CodeMetrics, Metric
from enum import Enum
from codebench_analytics.utils.components import Components
from codebench_analytics.assessments_filter import AssessmentFilter, AssessmentType
from os import path


class Code(Extractor):
    def collect(self, kinds: Optional[list[AssessmentType]] = None) -> str:
        pass

    def __collect(self, dataset_src: str, kinds: Optional[list[AssessmentType]]) -> Dict[str, str]:
        print("Collecting {} from {}".format(self.resource.value, dataset_src))
        execs = Components.get_users_data(dataset_src, self.resource)
        assessments_filtered = AssessmentFilter.get(dataset_src, kinds)
        code_statistics = {}

        for values in execs.values():
            for src in values:
                name = path.basename(src).split(".")[0]
                assessment_id, question_id = name.split("_", 1)
                assessment_id, question_id = int(assessment_id), int(question_id)

                if not assessment_id in assessments_filtered:
                    continue

                if not question_id in code_statistics:
                    code_statistics[question_id] = CodeMetrics()

                fullpath = path.join(dataset_src, src)
                with open(fullpath, "r") as log:
                    lines = log.readlines()
                    metrics: CodeMetrics = code_statistics[question_id]
                    i = 0

                    while i < len(lines):
                        l = lines[i].strip()
                        if l.startswith("== SUBMITION"):
                            pass
                        i += 1

        return code_statistics
