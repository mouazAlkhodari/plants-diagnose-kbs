from constant import *
from db import *
from gui import *
import codecs

randomChoice = True

''' asking helper functions '''
file = codecs.open('samples/test.txt', 'w', 'utf-8')


def Ask_Choices_Question(question: str, *choices) -> str:
    return showAskAboutSymtomWindow(question, choices)

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
    result = Ask_Choices_Question(
        'what is the plant to be diagnosed ?', *plants_Array)
    file.write(result + '\n')
    return result


def Ask_About_Symptom(question: str, symptom_Name, symptom_NameAr) -> float:
    if randomChoice:
        result = choice(list(CF_STRINGS.keys()))
        # result = 'مطلقاً'
        # result = 'لا'
        # result = 'لست متأكدا'
        # result = 'نعم ربما'
        # result = 'نعم بالتاكيد'
    else:
        result = Ask_Choices_Question(question, *CF_STRINGS.keys())
    file.write(symptom_NameAr + '\n')
    file.write(result + '\n')
    return CF_STRINGS[result]
