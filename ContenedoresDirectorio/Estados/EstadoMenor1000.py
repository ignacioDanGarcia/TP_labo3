from .EstadoContenedorAbstracta import EstadoContenedorAbstracta
from .EstadoMenor10000 import EstadoMenor10000


class EstadoMenor1000(EstadoContenedorAbstracta):
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.estado_siguiente = None
    
    def calcular_precio_adicional_estado(self, carga):

        medidas_int = self.contenedor.get_medidas_interior()
        if medidas_int.largo == carga.get_medidas().largo and medidas_int.ancho == carga.get_medidas().ancho and medidas_int.alto == carga.get_medidas().alto:
            return 210000
        elif medidas_int.comparar_medidas(carga.get_medidas()):
            return 1100 * (carga.peso / float(100))
        else:
            return False # porque no se me ocurre otra cosa jeje

    def condicion(self, distancia):
        return distancia < 1000

    def cambiar_estado_siguiente(self):
        self.estado_siguiente = EstadoMenor10000(self.contenedor)