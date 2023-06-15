import random
"""
supuestamente esta clase siempre va a dar un id distinto
"""

class GenerarId():
    def __init__(self) -> None:
        pass
    @staticmethod
    def generar_numeros_distintos():
        
        return random.randint(1, 100000)