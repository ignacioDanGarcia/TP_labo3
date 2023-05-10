from abc import ABC
from Medidas_contenedores import Medidas

class Contenedor(ABC):
    

    def __init__(self, id, precio_transporte):
        self.id = id
        self.precio_transporte = precio_transporte #Cada contenedor define un precio base que se debe pagar para transportar carga
        self.volumen_max = 0.0
        self.peso_max = 0.0
        self.medidas_interior = None
        self.medidas_exterior = None

    def get_medidas_interior(self):
        return self.medidas_interior
    
    def get_medidas_exterior(self):
        return self.medidas_exterior
    
    def get_id(self):
        return self.id
    
    def get_precio_transporte(self):
        return self.precio_transporte
    
    def get_volumen_max(self):
        return self.volumen_max
    
    def get_peso_max(self):
        return self.peso_max