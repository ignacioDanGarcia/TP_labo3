from BarcosDirectorio.Barcos import Barco
from ModuloGPS import ModuloGPS
from EmpresaDirectorio.CalculadorIngresosBarco import CalculadorIngresosBarco
class ModuloContable():
    def __init__(self) -> None:
        pass
    
    def calcular_ganancia_barco(self, barco :Barco, precio_gasolina, modulo_gps :ModuloGPS):
        nafta_gastada = barco.get_combustible_gastado()
        gasto_combustible = nafta_gastada * precio_gasolina
        
        calculadora_barco = CalculadorIngresosBarco()
        contenedores = barco.get_contenedores()
        distancia = modulo_gps.calcular_distancia()
        
        ganancia = 0
        for contenedor in contenedores:
            calculadora_barco.llenar_la_calculadora_precio_cargas(contenedor, distancia)
            ganancia += calculadora_barco.calcular_precio(contenedor,distancia)
        ganancia = ganancia - gasto_combustible
        return ganancia
