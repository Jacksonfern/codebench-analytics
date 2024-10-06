import csv
import logging
from os import makedirs, path
from typing import Any, Dict, List, Union

logger = logging.getLogger(__name__)


def save_dict(csvfile, data: Dict[int, Any], fields):
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    for key, value in data.items():
        writer.writerow({fields[0]: key, **vars(value)})


def save_list(csvfile, data: List[Any], fields):
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    for value in data:
        writer.writerow(value)


def save(
    base_src: str, filename: str, data: Union[list, dict], fields: List[str]
) -> str:
    if not path.exists(base_src):
        makedirs(base_src)
    if not filename.endswith(".csv"):
        filename += ".csv"

    src = path.join(base_src, filename)
    logging.info("generating '%s' file into '%s'", filename, src)

    with open(src, "w+") as csvfile:
        if isinstance(data, dict):
            save_dict(csvfile, data, fields)
        elif isinstance(data, list):
            save_list(csvfile, data, fields)
        else:
            raise ValueError("invalid data type {}".format(type(data)))

    return src
