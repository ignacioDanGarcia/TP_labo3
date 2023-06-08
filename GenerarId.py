import random
"""
supuestamente esta clase siempre va a dar un id distinto
"""

class GenerarId():
    def __init__(self):
        self.id_actual = 0
    
    def generar_numeros_distintos(self):
        
        return random.randint(1, 100000)