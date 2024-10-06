import json

import re
from typing import Optional

from codebench_analytics.extractor import Extractor
from codebench_analytics.utils.components import Components
from codebench_analytics.utils.assessments_filter import (
    AssessmentFilter,
    AssessmentType,
)
from os import path
import logging

from codebench_analytics.utils.dataset import save

logger = logging.getLogger(__name__)


class ActionsExtractor(Extractor):

    CORRECTED_INFO = "Congratulations, your code is correct!"
    NOT_JSON_METADATA = [
        "submit",
        "kill_program",
        "rename_file",
        "saida_testar",
        "dica_bullet",
        "dica_open",
    ]
    DATE_REGEX = re.compile(r"\d{4}-\d{1,2}-\d{1,2}\s\d{2}:\d{2}:\d{2}\.\d{3}")

    def extract_from(self, kinds: Optional[list[AssessmentType]] = None) -> str:
        data = []
        for src in self.dataset_src:
            logger.info("extracting '%s' from '%s'", self.resource.value, src)
            partial_data = self.__collect(src, kinds)
            data.extend(partial_data)

        csv_fields = [
            "semester",
            "class",
            "student",
            "assessment",
            "question",
            "event_time",
            "event_type",
            "event_op",
            "event_info",
        ]
        return save("output/data", "actions.csv", data, csv_fields)

    def __collect(
        self, dataset_src: str, kinds: Optional[list[AssessmentType]] = None
    ) -> list:
        user_events = Components.get_users_data(dataset_src, self.resource)
        assessments_filtered = AssessmentFilter.get(dataset_src, kinds)
        year = path.basename(dataset_src)
        rows = []

        for key, mirrors in user_events.items():
            class_, student = key.split("-")
            for mirror in mirrors:
                name = path.basename(mirror).split(".")[0]
                assessment_id, question_id = name.split("_")
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

                fullpath = path.join(dataset_src, mirror)
                with open(fullpath, "r") as log:
                    for line in log:
                        l = line.strip()
                        try:
                            values = re.fullmatch(r"([^#]*)#([^#]*)#(.*)", l)
                            if not values:
                                continue

                            event_time, event_type, metadata = values.groups()
                            if not ActionsExtractor.DATE_REGEX.fullmatch(event_time):
                                continue

                            row = {"event_time": event_time, "event_type": event_type}

                            if metadata and len(metadata) > 0:
                                if event_type not in ActionsExtractor.NOT_JSON_METADATA:
                                    meta_json = json.loads(metadata)
                                    if type(meta_json) == dict:
                                        if "origin" in meta_json:
                                            row["event_op"] = meta_json["origin"]
                                        if "key" in meta_json:
                                            row["event_info"] = meta_json["key"]
                                elif event_type == "submit":
                                    row["event_info"] = (
                                        "correct"
                                        if metadata == ActionsExtractor.CORRECTED_INFO
                                        else "incorrect"
                                    )

                            rows.append({**base_row, **row})
                        except:
                            values = re.fullmatch(r"([^#]*)#([^#]*)#(.*)", l)
                            print(values.groups())
                            print("error on line {}".format(l))
                            exit(0)
        return rows
