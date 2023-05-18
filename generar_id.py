"""
supuestamente esta clase siempre va a dar un id distinto
"""

class generar_id():
    def __init__(self):
        self.id_actual = 0
    
    def generar_numeros_distintos(self):
        id_generado = self.id_actual
        self.id_actual += 1
        return id_generado