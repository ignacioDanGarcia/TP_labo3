class Carga:

    def __init__(self, medidas, peso):
        self.__medidas = medidas
        self.__precio = 0.0
        self.__peso = peso

    def definir_precio_carga(self):
        #se define segun la carga: carga especial o simple
        #esto creo debe estar en otra clase para implementar principio de responsabiliddad unica
        
        #Buenis, donde dice que depende del tipo de carga? En el apartado de contenedores solo vo que dice que se suma el precio a pagar por la carga misma. 
        # Entiendo que la carga tendría un precio del producto que está adentro en sí y después se le suma al del contenedor por hacer el viaje.
        # El peso de la carga sería fijo y el del contenedor varía según la tabla de precios.
        pass
    
    'Getters y setters'
    def get_medidas(self):
        return self.__medidas
    def set_medidas(self,m):
        self.__medidas = m
    medidas = property(get_medidas,set_medidas)
    
    def get_precio(self):
        return self.__precio
    def set_precio(self, p):
        self.__precio = p
    precio = property(get_precio,set_precio)
    
    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso
    peso = property(get_peso,set_peso)
