import abc #para hacerla clase abstracta

class MetodosViajes(abc.ABC):
    @abc.abstractmethod
    def viajar():
        pass
    
    @abc.abstractmethod
    def definirPrecioViaje():
        pass