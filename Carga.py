class Carga:

    def __init__(self, medidas):
        self.medidas = medidas
        self.precio = 0.0

    def definir_precio_carga(self):
        #se define segun la carga: carga especial o simple
        #esto creo debe estar en otra clase para implementar principio de responsabiliddad unica
        pass

    def get_medidas(self):
        return self.medidas
    
    def get_precio(self):
        return self.precio

