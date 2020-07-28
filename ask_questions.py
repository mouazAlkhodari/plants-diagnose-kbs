from constant import *
from db import *
''' asking helper functions '''


def Ask_Choices_Question(question: str, *choices) -> str:
    '''
        function that ask question with list of choices to allow the user to choose from
    '''
    # // TODO make it in gui
    while True:
        try:
            answer = input('{}\nchoices:\n{}\nanswer:'.format(
                question,
                '\n'.join(
                    map(lambda choice: f"{choice[0] + 1}) {choice[1]}", enumerate(choices)))
            ))
            if answer in choices:
                return answer
            raise IOError(f'wrong choice Try Again')
        except IOError as error:
            print(f'{B_COLORS.FAIL}ERROR: {error}{B_COLORS.ENDC}')


def Ask_Plant_Name() -> str:
    return Ask_Choices_Question(f'{B_COLORS.OKBLUE}what is the plant to be diagnosed ?{B_COLORS.ENDC}', *plants_Array)


def Ask_About_Symptom(question: str) -> float:
    return CF_STRINGS[Ask_Choices_Question(question, *CF_STRINGS.keys())]
