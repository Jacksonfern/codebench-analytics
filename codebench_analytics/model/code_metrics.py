from dataclasses import dataclass
from typing import Optional


@dataclass
class SolutionMetrics:
    complexity: Optional[int] = None
    n_classes: Optional[int] = None
    n_functions: Optional[int] = None
    loc: Optional[int] = None
    lloc: Optional[int] = None
    sloc: Optional[int] = None
    comments: Optional[int] = None
    single_comments: Optional[int] = None
    multi_comments: Optional[int] = None
    blank_lines: Optional[int] = None
    h1: Optional[int] = None
    h2: Optional[int] = None
    N1: Optional[int] = None
    N2: Optional[int] = None
    h: Optional[int] = None
    N: Optional[int] = None
    calculated_N: Optional[int] = None
    volume: Optional[int] = None
    difficulty: Optional[int] = None
    effort: Optional[int] = None
    bugs: Optional[int] = None
    time: Optional[int] = None
    endmarker: Optional[int] = None
    name: Optional[int] = None
    number: Optional[int] = None
    string: Optional[int] = None
    newline: Optional[int] = None
    indent: Optional[int] = None
    dedent: Optional[int] = None
    lpar: Optional[int] = None
    rpar: Optional[int] = None
    lsqb: Optional[int] = None
    rsqb: Optional[int] = None
    colon: Optional[int] = None
    comma: Optional[int] = None
    semi: Optional[int] = None
    plus: Optional[int] = None
    minus: Optional[int] = None
    star: Optional[int] = None
    slash: Optional[int] = None
    vbar: Optional[int] = None
    amper: Optional[int] = None
    less: Optional[int] = None
    greater: Optional[int] = None
    equal: Optional[int] = None
    dot: Optional[int] = None
    percent: Optional[int] = None
    lbrace: Optional[int] = None
    rbrace: Optional[int] = None
    eq_equal: Optional[int] = None
    not_eq: Optional[int] = None
    less_eq: Optional[int] = None
    greater_eq: Optional[int] = None
    tilde: Optional[int] = None
    circumflex: Optional[int] = None
    lshift: Optional[int] = None
    rshift: Optional[int] = None
    dbl_star: Optional[int] = None
    plus_eq: Optional[int] = None
    minus_eq: Optional[int] = None
    star_eq: Optional[int] = None
    slash_eq: Optional[int] = None
    percent_eq: Optional[int] = None
    amper_eq: Optional[int] = None
    vbar_eq: Optional[int] = None
    circumflex_eq: Optional[int] = None
    lshift_eq: Optional[int] = None
    rshift_eq: Optional[int] = None
    dbl_star_eq: Optional[int] = None
    dbl_slash: Optional[int] = None
    dbl_slash_eq: Optional[int] = None
    at: Optional[int] = None
    at_eq: Optional[int] = None
    rarrow: Optional[int] = None
    ellipsis: Optional[int] = None
    colon_eq: Optional[int] = None
    op: Optional[int] = None
    error_token: Optional[int] = None
    comment: Optional[int] = None
    nl: Optional[int] = None
    encoding: Optional[int] = None
    number_int: Optional[int] = None
    number_float: Optional[int] = None
    kwd_and: Optional[int] = None
    kwd_or: Optional[int] = None
    kwd_not: Optional[int] = None
    kwd_none: Optional[int] = None
    kwd_false: Optional[int] = None
    kwd_true: Optional[int] = None
    kwd_as: Optional[int] = None
    kwd_assert: Optional[int] = None
    kwd_async: Optional[int] = None
    kwd_await: Optional[int] = None
    kwd_break: Optional[int] = None
    kwd_class: Optional[int] = None
    kwd_continue: Optional[int] = None
    kwd_def: Optional[int] = None
    kwd_del: Optional[int] = None
    kwd_if: Optional[int] = None
    kwd_elif: Optional[int] = None
    kwd_else: Optional[int] = None
    kwd_except: Optional[int] = None
    kwd_finally: Optional[int] = None
    kwd_for: Optional[int] = None
    kwd_while: Optional[int] = None
    kwd_import: Optional[int] = None
    kwd_from: Optional[int] = None
    kwd_global: Optional[int] = None
    kwd_in: Optional[int] = None
    kwd_is: Optional[int] = None
    kwd_lambda: Optional[int] = None
    kwd_nonlocal: Optional[int] = None
    kwd_pass: Optional[int] = None
    kwd_raise: Optional[int] = None
    kwd_return: Optional[int] = None
    kwd_try: Optional[int] = None
    kwd_with: Optional[int] = None
    kwd_yield: Optional[int] = None
    keyword: Optional[int] = None
    identifier: Optional[int] = None
    builtin_type: Optional[int] = None
    builtin_func: Optional[int] = None
    kwd_print: Optional[int] = None
    kwd_input: Optional[int] = None
    builtin_type_unique: Optional[int] = None
    builtin_func_unique: Optional[int] = None
    identifiers_unique: Optional[int] = None
    identifiers_max_len: Optional[int] = None
    identifiers_min_len: Optional[int] = None
    identifiers_mean_len: Optional[int] = None

    def as_list(self):
        return [
            self.periodo,
            self.turma,
            self.estudante,
            self.atividade,
            self.exercicio,
            self.complexity,
            self.n_classes,
            self.n_functions,
            self.loc,
            self.lloc,
            self.sloc,
            self.comments,
            self.single_comments,
            self.multi_comments,
            self.blank_lines,
            self.h1,
            self.h2,
            self.N1,
            self.N2,
            self.h,
            self.N,
            self.calculated_N,
            self.volume,
            self.difficulty,
            self.effort,
            self.bugs,
            self.time,
            self.endmarker,
            self.name,
            self.number,
            self.string,
            self.newline,
            self.indent,
            self.dedent,
            self.lpar,
            self.rpar,
            self.lsqb,
            self.rsqb,
            self.colon,
            self.comma,
            self.semi,
            self.plus,
            self.minus,
            self.star,
            self.slash,
            self.vbar,
            self.amper,
            self.less,
            self.greater,
            self.equal,
            self.dot,
            self.percent,
            self.lbrace,
            self.rbrace,
            self.eq_equal,
            self.not_eq,
            self.less_eq,
            self.greater_eq,
            self.tilde,
            self.circumflex,
            self.lshift,
            self.rshift,
            self.dbl_star,
            self.plus_eq,
            self.minus_eq,
            self.star_eq,
            self.slash_eq,
            self.percent_eq,
            self.amper_eq,
            self.vbar_eq,
            self.circumflex_eq,
            self.lshift_eq,
            self.rshift_eq,
            self.dbl_star_eq,
            self.dbl_slash,
            self.dbl_slash_eq,
            self.at,
            self.at_eq,
            self.rarrow,
            self.ellipsis,
            self.colon_eq,
            self.op,
            self.error_token,
            self.comment,
            self.nl,
            self.encoding,
            self.number_int,
            self.number_float,
            self.kwd_and,
            self.kwd_or,
            self.kwd_not,
            self.kwd_none,
            self.kwd_false,
            self.kwd_true,
            self.kwd_as,
            self.kwd_assert,
            self.kwd_async,
            self.kwd_await,
            self.kwd_break,
            self.kwd_class,
            self.kwd_continue,
            self.kwd_def,
            self.kwd_del,
            self.kwd_if,
            self.kwd_elif,
            self.kwd_else,
            self.kwd_except,
            self.kwd_finally,
            self.kwd_for,
            self.kwd_while,
            self.kwd_import,
            self.kwd_from,
            self.kwd_global,
            self.kwd_in,
            self.kwd_is,
            self.kwd_lambda,
            self.kwd_nonlocal,
            self.kwd_pass,
            self.kwd_raise,
            self.kwd_return,
            self.kwd_try,
            self.kwd_with,
            self.kwd_yield,
            self.keyword,
            self.identifier,
            self.builtin_type,
            self.builtin_func,
            self.kwd_print,
            self.kwd_input,
            self.builtin_type_unique,
            self.builtin_func_unique,
            self.identifiers_unique,
            self.identifiers_max_len,
            self.identifiers_min_len,
            self.identifiers_mean_len,
        ]
