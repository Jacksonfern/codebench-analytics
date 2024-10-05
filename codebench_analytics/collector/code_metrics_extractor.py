import os
import re

import numpy as np
import keyword
import token
import tokenize
from typing import Dict, List
from codebench_analytics.code_metrics import SolutionMetrics
import codebench_analytics.token_mapping as tkm

from collections import Counter, defaultdict

from radon.metrics import h_visit
from radon.raw import analyze
from radon.visitors import ComplexityVisitor


class Solution:

    __type_list = [
        "bool",
        "bytes",
        "bytearray",
        "complex",
        "dict",
        "float",
        "set",
        "int",
        "list",
        "range",
        "object",
        "str",
        "memoryview",
        "None",
        "frozenset",
    ]
    __builtin_types = set(__type_list)

    __f_list = [
        "abs",
        "all",
        "any",
        "ascii",
        "bin",
        "bool",
        "bytearray",
        "bytes",
        "callable",
        "chr",
        "classmethod",
        "compile",
        "delattr",
        "dir",
        "divmod",
        "enumerate",
        "eval",
        "exec",
        "filter",
        "format",
        "getattr",
        "globals",
        "hasattr",
        "hash",
        "hex",
        "id",
        "input",
        "isinstance",
        "issubclass",
        "iter",
        "len",
        "locals",
        "map",
        "max",
        "min",
        "next",
        "oct",
        "open",
        "ord",
        "pow",
        "print",
        "property",
        "range",
        "repr",
        "reversed",
        "round",
        "set",
        "setattr",
        "slice",
        "sorted",
        "staticmethod",
        "str",
        "sum",
        "super",
        "tuple",
        "type",
        "vars",
        "zip",
    ]
    __builtin_funcs = set(__f_list)

    @staticmethod
    def __is_builtin_func(name: str):
        return name in Solution.__builtin_funcs

    @staticmethod
    def __is_builtin_type(name: str):
        return name in Solution.__builtin_types

    @staticmethod
    def extract(base_src: str):
        data: List[SolutionMetrics] = []
        for code_filename in os.listdir(base_src):
            src = os.path.join(base_src, code_filename)
            solution = SolutionMetrics()

            metrics = Solution.__extract_solution_metrics(src)
            for attr, value in metrics.items():
                setattr(solution, attr, value)

            data.append(solution)
        return data

    @staticmethod
    def extract_from_professor(csv_src: str):
        data: Dict[SolutionMetrics] = {}
        with open(csv_src, "r") as csv_file:
            text = "".join(csv_file.readlines())
            solutions = re.split(r"#?\$#\$#\n|#!#!#", text)

            solution_id = -1
            for sol in solutions[2:]:
                if len(sol) == 0:
                    continue
                match = re.match(r"(\d+)", sol)
                if match:
                    solution_id = int(match.groups()[0])
                else:
                    assert solution_id != -1, "not found id for solution {}".format(sol)
                    tmp_code_src = "/tmp/code.py"

                    with open(tmp_code_src, "w+") as tmp_writer:
                        tmp_writer.write(sol)

                    solution = SolutionMetrics()

                    metrics = Solution.__extract_solution_metrics(tmp_code_src)
                    for attr, value in metrics.items():
                        setattr(solution, attr, value)

                    data[solution_id] = solution
                    solution_id = -1
        return data

    @staticmethod
    def __extract_solution_metrics(code_file_src: str):
        metrics = dict()
        with open(code_file_src) as f:
            codigo = "".join(f.readlines())

            try:
                v = ComplexityVisitor.from_code(codigo)
                metrics["complexity"] = v.complexity
                metrics["n_functions"] = len(v.functions)
                metrics["n_classes"] = len(v.functions)
            except BaseException as err:
                pass

            try:
                a = analyze(codigo)
                metrics["loc"] = a.loc
                metrics["lloc"] = a.lloc
                metrics["sloc"] = a.sloc
                metrics["blank_lines"] = a.blank
                metrics["comments"] = a.comments
                metrics["single_comments"] = a.single_comments
                metrics["multi_comments"] = a.multi
            except BaseException as err:
                pass

            try:
                h = h_visit(codigo)
                metrics["h1"] = h.total.h1
                metrics["h2"] = h.total.h2
                metrics["N1"] = h.total.N1
                metrics["N2"] = h.total.N2
                metrics["h"] = h.total.vocabulary
                metrics["N"] = h.total.length
                metrics["calculated_N"] = h.total.calculated_length
                metrics["volume"] = h.total.volume
                metrics["difficulty"] = h.total.difficulty
                metrics["effort"] = h.total.effort
                metrics["bugs"] = h.total.bugs
                metrics["time"] = h.total.time
            except BaseException as err:
                pass

            try:
                token_count = defaultdict(int)
                unique_identifiers = set()
                unique_strings = set()
                unique_btype = set()
                unique_bfunc = set()
                with tokenize.open(code_file_src) as f:
                    try:
                        tokens = tokenize.generate_tokens(f.readline)
                        for tk in tokens:
                            if tk.exact_type == token.NUMBER:
                                if "." in tk.string:
                                    token_count[tkm.NUMBER_FLOAT] += 1
                                else:
                                    token_count[tkm.NUMBER_INT] += 1
                            elif tk.type == token.NAME:
                                if keyword.iskeyword(tk.string):
                                    token_count[
                                        tkm.tk_codes.get(tk.string.lower(), tkm.KEYWORD)
                                    ] += 1
                                elif Solution.__is_builtin_type(tk.string):
                                    token_count[tkm.BUILTIN_TYPE] += 1
                                    unique_btype.add(tk.string)
                                elif Solution.__is_builtin_func(tk.string):
                                    if tk.string == "print":
                                        token_count[tkm.KWD_PRINT] += 1
                                    elif tk.string == "input":
                                        token_count[tkm.KWD_INPUT] += 1
                                    else:
                                        token_count[tkm.BUILTIN_FUNC] += 1
                                    unique_bfunc.add(tk.string)
                                else:
                                    token_count[tkm.IDENTIFIER] += 1
                                    unique_identifiers.add(tk.string)
                            elif tk.type == token.STRING:
                                token_count[tkm.STRING] += 1
                                unique_strings.add(tk.string)
                            else:
                                token_count[tk.exact_type] += 1
                    except BaseException as err:
                        pass

                for k, v in Counter(token_count).items():
                    metrics[tkm.tk_names[k]] = v

                metrics["builtin_type_unique"] = len(unique_btype)
                metrics["builtin_func_unique"] = len(unique_bfunc)
                metrics["identifiers_unique"] = len(unique_identifiers)
                metrics["identifiers_max_len"] = max(
                    [len(x) for x in unique_identifiers], default=0
                )
                metrics["identifiers_min_len"] = min(
                    [len(x) for x in unique_identifiers], default=0
                )
                metrics["identifiers_mean_len"] = np.mean(
                    [len(x) for x in unique_identifiers]
                )

            except BaseException as err:
                pass

        return metrics
