from experta import *
from functools import reduce, singledispatch

from custom_facts import *
from db.static import *


class Define_Plant_Diseases_Engine(KnowledgeEngine):

    @Rule(UserInput(plant=MATCH.plant), NOT(Fact(Diseases_Defined=True)))
    def define_Disease(self, plant):
        # print('define disease')
        for disease in Disease_Data[plant]:
            disease = {
                'plant': plant,
                **disease
            }
            self.declare(Build_Disease_Fact(**disease))

        self.declare(Fact(Diseases_Defined=True))


''' helper function in defining disease stage'''


def Accumulate_Symptoms_CF(resultSymptoms: dict, symptom: dict):
    symptomName = symptom['name']
    return {
        **resultSymptoms,
        symptomName: {
            'question': f"what about {symptomName}?",
            ** symptom,
        }
    }


def Build_Disease_Fact(**disease: Disease) -> Disease:
    return Disease(
        **{
            **disease,
            'symptoms': reduce(
                Accumulate_Symptoms_CF,
                disease['symptoms'],
                {}
            ),
            'state': disease['state'] if 'state' in disease else DiseaseStates.INITIAL,
        }
    )
