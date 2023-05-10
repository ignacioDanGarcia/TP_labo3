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


        #Un container con material especial (explosivos, desechos químicos o radioactivos) 
        # sólo puede ser transportado por un barco diseñado para tal fin.
        #los barcos de tipo básico, soportan contenedores con medidas del tipo basico
        # los barcos soportan cualquier contenedor cuyas medidas sean mayores a las de un contenedor básico. 
        #mi idea es resolver eso en puee_cargar_contenedor (cheque las medidas)
        
    @abstractmethod
    def puede_cargar_contenedor(self, contenedor):
        pass

    @abstractmethod
    def cargar(self, carga):
        #redefinir en cada clase que ereda de barco
        pass
