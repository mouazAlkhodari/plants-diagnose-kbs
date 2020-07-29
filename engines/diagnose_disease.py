from functools import reduce, singledispatch
from experta import *
from experta.utils import *

from custom_facts import *
from ask_questions import *
import codecs


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
        # # initialize
        # print('read', disease, repr(disease))
        Disease_Symptoms = diseaseSymptoms.values()
        UserInput_Symptoms_CF = unfreeze(userInputSymptoms) or {}

        # # processing
        total_CF = reduce(
            lambda resultCF, symptom: calcCF(
                resultCF,
                Symptom_CF_With_UserInput(symptom, UserInput_Symptoms_CF)
            ),
            Disease_Symptoms,
            0
        )
        # print('result', result_UserInput_Symptoms_CF)

        # updating
        self.modify(disease, CF=total_CF, state=DiseaseStates.DIAGNOSED)

    @Rule(NOT(Fact('done')), salience=-1)
    def get_results(self):
        results = []
        for factId in list(self.facts):
            if type(self.facts[factId]) is Disease:
                results.append((
                    factId,
                    self.facts[factId]['name'],
                    self.facts[factId]['CF']
                ))

        # Sorting the result Descending
        results = sorted(results, key=lambda x: x[2], reverse=True)

        file = codecs.open('samples/result.txt', 'w', 'utf-8')
        file.write(
            json.dumps(
                unfreeze(self.facts[results[0][0]]), indent=3, ensure_ascii=False
            ) + '\n\n'
        )
        file.write(json.dumps(results, indent=3, ensure_ascii=False))
        print(results)
        self.declare(Fact('done'))


def Symptom_CF_With_UserInput(symptom: dict, userInputSymptomsCF: dict):
    symptomName = symptom['name']
    symptomCF = symptom['CF']
    return symptomCF * userInputSymptomsCF[symptomName]


def calcCF(cf1, cf2):
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    if cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))
