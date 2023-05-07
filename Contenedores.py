import abc #para hacerla clase abstracta

class Medidas:
    def __init__(self, largoInterior, anchoInterior, altoInterior, largoExt, anchoExt, altoExt):
        self.largoInterior = largoInterior
        self.anchoInterior = anchoInterior
        self.altoInterior = altoInterior
        self.largoExt = largoExt
        self.anchoExt = anchoExt
        self.altoExt = altoExt


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
    