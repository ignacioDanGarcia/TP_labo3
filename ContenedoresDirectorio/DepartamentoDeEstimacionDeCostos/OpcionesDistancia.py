from enum import Enum

class OpcionesDistancia(Enum):
    MENOR100 = (200000, 1000)
    MENOR1000 = (210000, 1100)
    MENOR10000 = (230000, 1150)
    MAS10000 = (250000, 1500)