from .EstadoContenedorAbstracta import EstadoContenedorAbstracta
from .EstadoMenor1000 import EstadoMenor1000


class EstadoMenor100(EstadoContenedorAbstracta):
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.estado_siguiente = None
    
    def calcular_precio_adicional_estado(self, carga):

        medidas_int = self.contenedor.get_medidas_interior()
        if medidas_int.largo == carga.get_medidas().largo and medidas_int.ancho == carga.get_medidas().ancho and medidas_int.alto == carga.get_medidas().alto:

            return 200000
        elif medidas_int.comparar_medidas(carga.get_medidas()):
            
            return 1000 * (carga.peso / float(100))
        else:
            return False # porque no se me ocurre otra cosa jeje

    def condicion(self, distancia):
        return distancia < 100

    def cambiar_estado_siguiente(self):
        self.estado_siguiente = EstadoMenor1000(self.contenedor)
        
        
    
        
