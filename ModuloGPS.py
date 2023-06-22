import random
from Excepciones.exceptions import tiempo_incorrecto,distancia_incorrecta
class ModuloGPS:
    def __init__(self) -> None:
          pass
   
    def calcular_distancia(self):
        return random.randint(1, 20000) #KMS
    def calcular_tiempo(self):
        return random.randint(1, 1200) #HS Tiempo promedio de viajes de barcos con contenedores de carga según Google
    
    def check_valores(self):
        horas = self.calcular_tiempo()
        if horas <= 0:
            raise tiempo_incorrecto("No es posible viajar esta distancia")
        distancia = self.calcular_distancia()
        if distancia <= 0:
            raise distancia_incorrecta("No es posible viajar distancia negativa o 0 kms")