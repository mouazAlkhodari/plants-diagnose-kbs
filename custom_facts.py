from experta import *
from schema import *

from constant import *
''' Custom Defined Facts '''


class Disease(Fact):
    # Description: Defines the types of data describing the details of a Disease
    #
    # Properties:
    # -- name - Name of the disease
    # -- plant - Name of the plant that the disease belongs to
    # -- symptoms - The disease symptoms. It's dict object that map Name of the Symptom with symptoms data
    #             -- Symptom object have CF property that is the symptom contributes to the overall disease
    # -- CF - The total weight that the symptoms of the disease contribute. It's an addition of only the present symptoms.
    # -- state - The current state/stage of the disease in the system

    name = Field(str, mandatory=True)

    plant = Field(str, mandatory=True)
    symptoms = Field({str: dict}, mandatory=True)

    CF: Field(float)
    state: Field(DiseaseStates.values, DiseaseStates.INITIAL)


class UserInput(Fact):
    plant = Field(str, mandatory=True)
    symptoms = Field(
        Or({str: float}, object),
    )
