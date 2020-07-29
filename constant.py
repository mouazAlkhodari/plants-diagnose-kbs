
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
    'نعم بالتاكيد':
    0.9,
    'نعم ربما':
    0.3,
    'لست متأكدا':
    0,
    'لا':
    -0.3,
    'مطلقاً':
    -0.8,
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


TITLE = 'Plant Diagnose - تشخيص أمراض المزروعات'
WELCOME = 'أهلا بك في برنامج خبير تشخيص أمراض المزروعات'
START = 'إبدا'
BACKGROUND = 'assets/background.png'
