
''' helper constant '''


class B_COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


CF_STRINGS = {
    'Yes': 1.0,
    'No': 0.0
}


class DiseaseStates:
    INITIAL = 'INITIAL'
    SY_CF_INPUTTED = 'SY_CF_INPUTTED'
    DIAGNOSED = 'DIAGNOSED'

    values = [
        'INITIAL',
        'SY_CF_INPUTTED',
        'DIAGNOSED'
    ]
