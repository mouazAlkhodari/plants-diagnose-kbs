from .disease_data import *

import json
from random import *
from math import *
from constant import *

for plant in plants_Array:
    symptoms = {}
    print("!!", plant)
    print("disease cnt", len(Disease_Data[plant]))
    for disease in Disease_Data[plant]:
        for symptom in list(disease['symptoms']):
                symptoms[symptom['name']] = choice(list(CF_STRINGS.keys()))
    print("symptoms cnt", len(symptoms))
