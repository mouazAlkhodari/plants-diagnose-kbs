from functools import reduce, singledispatch
from experta import *
from experta.utils import *

from custom_facts import *
from ask_questions import *


class Diagnose_Disease_Engine(KnowledgeEngine):

    @Rule(
        AS.userInput << UserInput(
            plant=MATCH.userInputPlant,
            symptoms=MATCH.userInputSymptoms,
        ),
        AS.disease << Disease(
            plant=MATCH.diseasePlant,
            symptoms=MATCH.diseaseSymptoms,
            state=DiseaseStates.SY_CF_INPUTTED,
        ),
        TEST(lambda diseasePlant, userInputPlant: diseasePlant == userInputPlant),
        # may Test the cf Here or inside the RHS
    )
    def Diagnose_Disease(
            self,
            diseaseSymptoms: dict,
            disease: Disease,
            userInputSymptoms: dict,
    ):
        # pass
        # # initialize
        # print('read', disease, repr(disease))
        Disease_Symptoms = diseaseSymptoms.values()
        UserInput_Symptoms_CF = unfreeze(userInputSymptoms) or {}

        # # processing
        total_CF = 1 - reduce(
            lambda resultCF, symptom: calcCF(
                resultCF,
                Calc_Symptom_CF_With_UserInput(symptom, UserInput_Symptoms_CF)
            ),
            Disease_Symptoms,
            1
        )
        # print('result', result_UserInput_Symptoms_CF)

        # updating
        self.modify(disease, CF=total_CF, state=DiseaseStates.DIAGNOSED)


def Calc_Symptom_CF_With_UserInput(symptom: dict, userInputSymptomsCF: dict):
    symptomName = symptom['name']
    symptomCF = symptom['CF']
    return symptomCF * userInputSymptomsCF[symptomName]


def calcCF(cf1, cf2):
    # print(cf1 * (1 - cf2))
    return cf1 * (1 - cf2)
    # TODO: check if it worked
