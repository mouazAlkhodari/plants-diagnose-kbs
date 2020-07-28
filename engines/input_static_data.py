from experta import *

from custom_facts import *
from ask_questions import *

class Input_Static_Data_Engine(KnowledgeEngine):

    @Rule(NOT(UserInput(plant=W())))
    def read_Plant_Name(self):
        # print('read plant')
        self.declare(UserInput(
            plant=Ask_Plant_Name(),
            symptoms={}
        ))
