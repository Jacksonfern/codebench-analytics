class SolutionMetrics:
    def __init__(self) -> None:
        self.complexity = None
        self.n_classes = None
        self.n_functions = None
        self.loc = None
        self.lloc = None
        self.sloc = None
        self.comments = None
        self.single_comments = None
        self.multi_comments = None
        self.blank_lines = None
        self.h1 = None
        self.h2 = None
        self.N1 = None
        self.N2 = None
        self.h = None
        self.N = None
        self.calculated_N = None
        self.volume = None
        self.difficulty = None
        self.effort = None
        self.bugs = None
        self.time = None
        self.endmarker = None
        self.name = None
        self.number = None
        self.string = None
        self.newline = None
        self.indent = None
        self.dedent = None
        self.lpar = None
        self.rpar = None
        self.lsqb = None
        self.rsqb = None
        self.colon = None
        self.comma = None
        self.semi = None
        self.plus = None
        self.minus = None
        self.star = None
        self.slash = None
        self.vbar = None
        self.amper = None
        self.less = None
        self.greater = None
        self.equal = None
        self.dot = None
        self.percent = None
        self.lbrace = None
        self.rbrace = None
        self.eq_equal = None
        self.not_eq = None
        self.less_eq = None
        self.greater_eq = None
        self.tilde = None
        self.circumflex = None
        self.lshift = None
        self.rshift = None
        self.dbl_star = None
        self.plus_eq = None
        self.minus_eq = None
        self.star_eq = None
        self.slash_eq = None
        self.percent_eq = None
        self.amper_eq = None
        self.vbar_eq = None
        self.circumflex_eq = None
        self.lshift_eq = None
        self.rshift_eq = None
        self.dbl_star_eq = None
        self.dbl_slash = None
        self.dbl_slash_eq = None
        self.at = None
        self.at_eq = None
        self.rarrow = None
        self.ellipsis = None
        self.colon_eq = None
        self.op = None
        self.error_token = None
        self.comment = None
        self.nl = None
        self.encoding = None
        self.number_int = None
        self.number_float = None
        self.kwd_and = None
        self.kwd_or = None
        self.kwd_not = None
        self.kwd_none = None
        self.kwd_false = None
        self.kwd_true = None
        self.kwd_as = None
        self.kwd_assert = None
        self.kwd_async = None
        self.kwd_await = None
        self.kwd_break = None
        self.kwd_class = None
        self.kwd_continue = None
        self.kwd_def = None
        self.kwd_del = None
        self.kwd_if = None
        self.kwd_elif = None
        self.kwd_else = None
        self.kwd_except = None
        self.kwd_finally = None
        self.kwd_for = None
        self.kwd_while = None
        self.kwd_import = None
        self.kwd_from = None
        self.kwd_global = None
        self.kwd_in = None
        self.kwd_is = None
        self.kwd_lambda = None
        self.kwd_nonlocal = None
        self.kwd_pass = None
        self.kwd_raise = None
        self.kwd_return = None
        self.kwd_try = None
        self.kwd_with = None
        self.kwd_yield = None
        self.keyword = None
        self.identifier = None
        self.builtin_type = None
        self.builtin_func = None
        self.kwd_print = None
        self.kwd_input = None
        self.builtin_type_unique = None
        self.builtin_func_unique = None
        self.identifiers_unique = None
        self.identifiers_max_len = None
        self.identifiers_min_len = None
        self.identifiers_mean_len = None

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
