from abc import ABC, abstractmethod
from Contenedores import Contenedor

class Barco(ABC):
    def __init__(self, id, peso_max, cant_contenedores_max):
        self.id = id
        self.disponible = True
        self.peso_max = peso_max
        self.cant_contenedores_max = cant_contenedores_max
        self.kmRecorrido = 0

        #saque las vriables de medidas interior y exterior ya que el enunciado solo habla de las medidas de 
        # los contenedores contenedores.
        #contenedores:Todos los barcos poseen una estructura especializada que permite organizar, asegurar 
        # y transportar los contenedores. En el caso de los barcos de tipo básico, dicha estructura sólo
        #  está diseñada para soportar contenedores cuyas dimensiones coincidan con las de un contenedor de 
        # tipo básico.mientras que en el caso de los barcos especializados dicha estructura permite transportar 
        # cualquier tipo de contenedor cuyas medidas sean superiores a las de un contenedor básico. 
        #este punto lo trato en el metodo puede_cargar_contenedor(self, contenedor):
    @abstractmethod
    def puede_cargar_contenedor(self, contenedor):
        pass

    @abstractmethod
    def cargar(self, carga):
        #redefinir en cada clase que ereda de barco
        pass
