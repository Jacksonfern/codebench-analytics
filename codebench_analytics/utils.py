from os import makedirs, path
import csv
import logging
from typing import Any, Dict, List, Union


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
    logging.info("Generating {} file into {}...".format(filename, src))

    with open(src, "w+") as csvfile:
        if type(data) == dict:
            save_dict(csvfile, data, fields)
        elif type(data) == list:
            save_list(csvfile, data, fields)
        else:
            raise Exception("Invalid data type {}".format(type(data)))

    logging.info("Done!")

    return src


def codeDiff(prev_code, cur_code) -> int:
    diff = 0
    n = len(prev_code)
    m = len(cur_code)
    for i in range(n):
        prev_line = prev_code[i]
        cur_line = cur_code[i] if i < m else ""
        diff += sum(1 for a, b in zip(prev_line, cur_line) if a != b) + abs(
            len(prev_line) - len(cur_line)
        )

    for i in range(n, m):
        diff += len(cur_code[i])
    return diff
