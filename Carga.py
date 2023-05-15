class Carga:

    def __init__(self, medidas):
        self.medidas = medidas
        self.precio = 0.0

    def definir_precio_carga(self):
        #se define segun la carga: carga especial o simple
        #esto creo debe estar en otra clase para implementar principio de responsabiliddad unica
        
        #Buenis, donde dice que depende del tipo de carga? En el apartado de contenedores solo vo que dice que se suma el precio a pagar por la carga misma. 
        # Entiendo que la carga tendría un precio del producto que está adentro en sí y después se le suma al del contenedor por hacer el viaje.
        # El peso de la carga sería fijo y el del contenedor varía según la tabla de precios.
        pass

    def get_medidas(self):
        return self.medidas
    
    def get_precio(self):
        return self.precio

