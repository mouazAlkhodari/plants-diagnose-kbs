from experta import *
from schema import *
from experta.utils import *
from functools import reduce, singledispatch

from engines import *

''' engines '''



class Plants_Disease_Diagnose_Engine(
    Input_Static_Data_Engine,
    Define_Plant_Diseases_Engine,
    Input_Symptoms_CF_Engine,
    Diagnose_Disease_Engine,
    KnowledgeEngine,
):
    pass


watch('ACTIVATIONS')
engine = Plants_Disease_Diagnose_Engine()

engine.reset()
engine.run()

print(engine.facts)
