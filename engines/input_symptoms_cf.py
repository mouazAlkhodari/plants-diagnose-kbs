from functools import reduce, singledispatch
from experta.utils import *
from experta import *

from custom_facts import *
from ask_questions import *


class Input_Symptoms_CF_Engine(KnowledgeEngine):

    @ Rule(
        AS.userInput << UserInput(
            plant=MATCH.userInputPlant,
            symptoms=MATCH.userInputSymptoms,
        ),
        AS.disease << Disease(
            plant=MATCH.diseasePlant,
            symptoms=MATCH.diseaseSymptoms,
            state=DiseaseStates.INITIAL,
        ),
        TEST(lambda diseasePlant, userInputPlant: diseasePlant == userInputPlant)
    )
    def read_Disease_Symptoms_CF(
            self,
            userInput: UserInput,
            diseaseSymptoms: dict,
            disease: Disease,
            userInputSymptoms: dict,
    ):
        # initialize
        # print('read', userInput, repr(userInput), disease, repr(disease))
        Disease_Symptoms = diseaseSymptoms.values()
        UserInput_Symptoms_CF = unfreeze(userInputSymptoms) or {}

        # processing
        result_UserInput_Symptoms_CF = reduce(
            Accumulate_UserInput_Symptoms_CF,
            Disease_Symptoms,
            UserInput_Symptoms_CF
        )

        # print('result', result_UserInput_Symptoms_CF)

        # updating
        self.modify(userInput, symptoms=result_UserInput_Symptoms_CF)
        self.modify(disease, state=DiseaseStates.SY_CF_INPUTTED)


''' helper function in reading symptoms CF stage'''


def Accumulate_UserInput_Symptoms_CF(resultSymptomsCF: dict, symptom: dict) -> dict:
    # print('\nX\n', resultSymptomsCF, '\nW\n', symptom)
    symptom_Name = symptom['name']
    symptom_NameAr = symptom['nameAr']
    symptom_Question = symptom['question']

    return {
        **resultSymptomsCF,
        # //TODO add custom questions
        symptom_Name: Ask_About_Symptom(symptom_Question,symptom_Name,symptom_NameAr)if
        not symptom_Name in resultSymptomsCF else
        resultSymptomsCF[symptom_Name],
    }
