import abc #para hacerla clase abstracta

class Medidas:
    def __init__(self, largoInterior, anchoInterior, altoInterior, largoExt, anchoExt, altoExt):
        self.largoInterior = largoInterior
        self.anchoInterior = anchoInterior
        self.altoInterior = altoInterior
        self.largoExt = largoExt
        self.anchoExt = anchoExt
        self.altoExt = altoExt
"""
creo que debemos usar la clase crga, hay una regla de negocio de no cargar una carga que supere la medidas del container
class Carga:
    def __init__(self, medidas, precio):
        self.medidas = madidas
        self.precio = precio
        
class Contenedores(abc.ABC):
    
    def __init__(self, id, volumen, peso, medidas):
        self.id = id
        self.volumen = volumen
        self.peso = peso
        self.medidas = medidas
    
    
    @abc.abstractmethod
    def getVolumen(self):
        pass
        
    @abc.abstractmethod
    def cargar(self, carga):
        pass
"""

class Contenedores(abc.ABC):
    
    def __init__(self, id, volumen, precioCarga, peso, medidas):
        self.id = id
        self.volumen = volumen
        self.precioCarga = precioCarga
        self.peso = peso
        self.medidas = medidas
    
    
    @abc.abstractmethod
    def getVolumen(self):
        pass
    
