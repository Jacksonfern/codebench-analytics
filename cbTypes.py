from enum import Enum, unique

@unique
class Data(Enum):
    ASSESSMENT = 'assessments'
    USER = 'users'

@unique
class Resource(Enum):
    CODEMIRRORS = 'codemirror'
    EXECUTIONS = 'executions'
    CODES = 'codes'
    GRADES = 'grades'
    MOUSE_MOVES = 'mousemove'

    EVENTS = 'eventos.log'
    LOGINS = 'logins.log'
    USERS_INFO = 'user.data'

@unique
class QuestionExecution(Enum):
    NONE = 0,
    SUBMIT = 1,
    TEST = 2,

@unique
class QuestionStatus(Enum):
    BLANK = 0,
    CORRECT = 1,
    INCORRECT = 2,
    GENERAL_ERROR = 3,
    SYNTAX_ERROR = 4,