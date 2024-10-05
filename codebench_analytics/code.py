# ***********************USELESS FOR NOW*************************************

from typing import Dict, List
from metrics import CodeMetrics, Metric
from enum import Enum
from components import Components
from codebench_analytics.assessments_filter import AssessmentFilter
from os import path
import re

class Code(Metric):
    def __init__(self, *dataset_src, resource: Enum):
        super().__init__(*dataset_src, resource=resource)

    def collect(self, kinds: List[str]) -> None:
        pass

    def __collect(self, dataset_src: str, kinds = List[str]) -> Dict[str, str]:
        print('Collecting {} from {}'.format(self.resource.value, dataset_src))
        execs = Components.getUsersData(dataset_src, self.resource)
        assessments_filtered = AssessmentFilter.get(dataset_src, kinds)
        code_statistics = {}

        for values in execs.values():
            for src in values:
                name = path.basename(src).split('.')[0]
                assessment_id, question_id = name.split('_', 1)
                assessment_id, question_id = int(assessment_id), int(question_id)

                if not assessment_id in assessments_filtered:
                    continue

                if not question_id in code_statistics:
                    code_statistics[question_id] = CodeMetrics()

                fullpath = path.join(dataset_src, src)
                with open(fullpath, 'r') as log:
                    lines = log.readlines()
                    metrics: CodeMetrics = code_statistics[question_id]
                    i = 0

                    while i < len(lines):
                        l = lines[i].strip()
                        if l.startswith('== SUBMITION'):
                            pass
                        i += 1
        
        return code_statistics
