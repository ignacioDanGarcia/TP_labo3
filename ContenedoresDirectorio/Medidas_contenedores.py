class Medidas:

    def __init__(self, largo, ancho, alto):
        self.__largo = largo
        self.__ancho = ancho
        self.__alto = alto

    def get_alto(self):
        return self.__alto
    def set_alto(self, al):
        self.__alto = al
    alto = property(get_alto,set_alto)
    
    
    def get_ancho(self):
        return self.__ancho
    def set_ancho(self, an):
        self.__ancho = an
    ancho = property(get_ancho,set_ancho)
    
    def get_largo(self):
        return self.__largo
    def set_largo(self,lar):
        self.__largo = lar
    largo = property(get_largo,set_largo)
    
    def comparar_medidas(self, medidas):
        #devuelve FAlSE si las medidas pasadas por parametro son mayores a las de la instancia
        #devuelve TRUE si las medidas pasadas x parametro son menores o iguales a las de la instancia

        alto = False
        largo = False
        ancho = False

        if medidas.get_alto <= self.get_alto:
            alto = True
        
        if medidas.get_ancho <= self.get_ancho:
            ancho = True
        
        if medidas.get_largo <= self.get_largo:
            largo = True

        return alto and largo and ancho
