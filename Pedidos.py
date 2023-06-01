from Carga import Carga
import random
from generar_id import generar_id

class Pedidos:
    gen = generar_id()
    def __init__(self, retiraEnPuerto, conteneCompleto, cargas, necesitaTransporte):
        self.__retiraEnPuerto = retiraEnPuerto #bool
        self.__conteneCompleto = conteneCompleto #bool
        self.__id = Pedidos.gen.generar_numeros_distintos()
        self.__cargas = cargas
        self.__necesitaTransporte = necesitaTransporte #bool si es False no sumamos el precio de 
                                                       #transporte carga x camion en el costo total del pedido
        'pruebas de git'
    
    'Getters y setters:'

    def get_necesitaTransporte(self):
        return self.__necesitaTransporte

    def get_id(self):
        return self.__id
    
    def get_retiraEnPuerto(self):
        return self.__retiraEnPuerto
    def set_retiraEnPuerto(self, ret):
        self.__retiraEnPuerto = ret
    retiraEnPuerto = property(get_retiraEnPuerto,set_retiraEnPuerto)

    def get_conteneCompleto(self):
        return self.__conteneCompleto
    def set_conteneCompleto(self, completo):
        self.__conteneCompleto = completo
    conteneCompleto = property(get_conteneCompleto,set_conteneCompleto)

    
    def get_cargas(self):
        return self.__cargas
    def set_cargas(self, cargas):
        self.__cargas.append(cargas)
    cargas = property(get_cargas,set_cargas)
        