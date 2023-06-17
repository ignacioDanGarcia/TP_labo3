from .OpcionesDistancia import OpcionesDistancia
from Excepciones.exceptions import distancia_incorrecta

class SelectoraEstrategiaPrecio():
    def __init__(self) -> None:
        pass
    
    def estrategia_por_categoria(self, distancia):
        estrategias = {
            OpcionesDistancia.MENOR100.value: (distancia > 0 and distancia < 100),
            OpcionesDistancia.MENOR1000.value: (distancia > 100 and distancia < 1000),
            OpcionesDistancia.MENOR10000.value: (distancia > 1000 and distancia < 10000),
            OpcionesDistancia.MAS10000.value: distancia > 10000
        }

        for enum_valor, condicion in estrategias.items():
            if condicion:
                return enum_valor
        
        raise distancia_incorrecta("La distancia especificada no cumple con ningún caso")
        

