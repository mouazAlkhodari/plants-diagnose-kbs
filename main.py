from functools import reduce, singledispatch

from experta import *
from experta.utils import *
from schema import *

from db import *
from engines import *
from gui import *

try:
    # ReadAndConvert()
    import db.disease_data
except:
    ReadAndConvert()


class Plants_Disease_Diagnose_Engine(
    Input_Static_Data_Engine,
    Define_Plant_Diseases_Engine,
    Input_Symptoms_CF_Engine,
    Diagnose_Disease_Engine,
    KnowledgeEngine,
):
    pass


if showStartWindow():

    # watch('ACTIVATIONS')
    engine = Plants_Disease_Diagnose_Engine()

    engine.reset()
    engine.run()


'''
    sg.theme(sg.THEME_CLASSIC)  # please make your windows colorful

    layout = [
        [
            sg.Text('ما هي نسبة وجود العرض ؟',size=(800, 1), justification='center')],
        [
            sg.Frame(
                title="options",
                layout=[
                    [sg.Radio('مؤكدة', 'g1',size=(800,1))],
                    [sg.Radio('محتملة', 'g1',size=(800,1))],
                    [sg.Radio('مستحيلة', 'g1',size=(800,1))]
                ],
                element_justification='center'
                ,size=(800,1)
            ),
        ],
        [sg.Ok(), sg.Cancel()]
    ]


    # Create the Window
    window = sg.Window('SHA-1 & 256 Hash', layout,font=("Helvetica", 18),size=(800,600))

    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()
    
'''
