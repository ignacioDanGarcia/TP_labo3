from abc import ABC, abstractmethod
from Medidas import Medidas
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, medidas_incorrectas

class Contenedor(ABC):
    

    def __init__(self, id, precio_transporte):
        self.id = id
        self.precio_transporte = precio_transporte #Cada contenedor define un precio base que se debe pagar para transportar carga
        self.volumen_max = 0.0
        self.peso_max = 0.0
        self.medidas_interior = None
        self.medidas_exterior = None
        self.carga = None

        #algo hay que hacer con este punto:
        # Un contenedor sin características especiales no puede transportar material especial.
        #Creo que con un booleano de si es apto para material especial en el contructor podría ir este punto así 

    def get_medidas_interior(self):
        return self.medidas_interior
    
    def get_medidas_exterior(self):
        return self.medidas_exterior
    
    def get_id(self):
        return self.id
    
    def get_precio_transporte(self):
        return self.precio_transporte
    
    def get_volumen_max(self):
        return self.volumen_max
    
    def get_peso_max(self):
        return self.peso_max
    
    #Cualquier carga cuyas  medidas o peso supere lo definido en el container no podrá 
    # ser trasladada en el mismo.
    def verificar_carga(self, carga):
        no_supera_medidas = False
        no_supera_peso_max = False
        no_supera_vol_max = False
        try:
            if self.medidas_interior.comparar_medidas(carga.get_medidas()):
                no_supera_medidas = True

            if carga.get_peso() < self.get_peso_max():
                no_supera_peso_max = True

            if carga.get_volumen() < self.get_volumen_max():
                no_supera_vol_max = True
            
            if (no_supera_peso_max and no_supera_medidas and no_supera_vol_max):
                return True
        except medidas_incorrectas as e:
            print(str(e))
        else:
            #excepcion catcheada en calcular_precio_adicional de empresa
            raise contenedor_no_puede_llevar_carga("La carga no puede ser transportada por este contenedor")

    
    def cargar(self, carga):
        if self.verificar_carga(carga):
            self.carga = carga
    
    def peso_contenedor(self):
        return self.carga.get_peso()