from Excepciones.exceptions import medidas_incorrectas
class Medidas:

    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def get_alto(self):
        return self.alto
    
    def get_ancho(self):
        return self.ancho
    
    def get_largo(self):
        return self.largo
    
    def comparar_medidas(self, medidas):
        #devuelve FAlSE si las medidas pasadas por parametro son mayores a las de la instancia
        #devuelve TRUE si las medidas pasadas x parametro son menores o iguales a las de la instancia

        alto = False
        largo = False
        ancho = False

        if 0 < medidas.get_alto <= self.get_alto:
            alto = True
        
        if 0 < medidas.get_ancho <= self.get_ancho:
            ancho = True
        
        if 0 < medidas.get_largo <= self.get_largo:
            largo = True

        if (alto and largo and ancho):
            return True
        raise medidas_incorrectas("La carga no puede ser transportada por este contenedor")
