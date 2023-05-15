from Cargable import Cargable
from abc import ABC, abstractmethod
class Barco(Cargable, ABC):
    def __init__(self, id, peso_max, cant_contenedores_max, lleva_mat_esp):
        self.__id = id
        self.__disponible = True
        self.__peso_max = peso_max
        self.__cant_contenedores_max = cant_contenedores_max
        self.__kmRecorridos = 0
        self.__lleva_mat_esp = lleva_mat_esp
        self.__contenedores = []
        
        #saque las vriables de medidas interior y exterior ya que el enunciado solo habla de las medidas de 
        # los contenedores contenedores.


        #CONTAINER MATERIAL ESPECIAL (explosivos, desechos químicos o radioactivos) 
        # sólo puede ser transportado por un barco diseñado para tal fin.
        #los barcos de tipo básico, soportan contenedores con medidas del tipo basico
        # los barcos soportan cualquier contenedor cuyas medidas sean mayores a las de un contenedor básico. 
        #mi idea es resolver eso en puee_cargar_contenedor (cheque las medidas)
    
    #Agrego getters y setters.
    def get_id(self):
        return self.__id
    def set_id(self):
        self.__id = id
    id = property(get_id,set_id)
    
    def get_peso_max(self):
        return self.__peso_max
    def set_peso_max(self,peso):
        self.__peso_max = peso
    peso_max = property(get_peso_max,set_peso_max)
    
    def get_cant_contenedores_max(self):
        return self.__cant_contenedores_max 
    def set_cant_contenedores_max(self, cant):
        self.__cant_contenedores_max = cant
    cant_contenedores_max = property(get_cant_contenedores_max,set_cant_contenedores_max)
    
    def get_lleva_mat_esp(self):
        return self.__lleva_mat_esp
    def set_lleva_mat_esp(self, lleva):
        self.__lleva_mat_esp = lleva
    lleva_mat_esp = property(get_lleva_mat_esp,set_lleva_mat_esp)
    
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,dispo):
        self.__disponible = dispo
    disponible = property(get_disponible,set_disponible)
    
    def get_km_recorridos(self):
        return self.__kmRecorridos
    def set_km_recorridos(self, kms):
        self.__kmRecorridos = kms
    km_recorridos = property(get_km_recorridos,set_km_recorridos)
    
    def get_contenedores(self):
        return self.__contenedores
    def set_contenedores(self,contenedores):
        self.__contenedores = contenedores
    contenedores = property(get_contenedores,set_contenedores)
        
    
    def obtener_peso_actual(self):
        peso = 0
        for contenedor in self.contenedores:
            peso += contenedor.get_carga().get_peso()
        return peso
    
    #chequeo el material del contenedor y si la capacidad max de contenedores no esta cubierta
    # si se supera el max de contenedores agregar excepcion  
    @abstractmethod
    def puede_cargar_contenedor(self, contenedor):
        pass

    @abstractmethod
    def cargar(self, carga):
        #redefinir en cada clase que hereda de barco
        pass
