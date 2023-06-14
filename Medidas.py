from Excepciones.exceptions import medidas_incorrectas
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
        # Devuelve False si las medidas pasadas por parámetro son mayores o iguales a las de la instancia
        # Devuelve True si las medidas pasadas por parámetro son menores estrictamente a las de la instancia

        alto = False
        largo = False
        ancho = False

        if 0 < medidas.get_alto() <= self.get_alto():
            alto = True
            
        if 0 < medidas.get_ancho() <= self.get_ancho():
            ancho = True
            
        if 0 < medidas.get_largo() <= self.get_largo():
            largo = True

        if alto and largo and ancho:
            return True
        
        # Excepción capturada en verificar_carga() de Contenedor
        #raise medidas_incorrectas("La carga no puede ser transportada por este contenedor") 
        # #-- La idea va a ser que recorra todos los contenedores posibles para ver donde puede meter la carga. 
        #Si tiramos excepción se cortaría el programa y no podría verificar más excepciones. 
        return False