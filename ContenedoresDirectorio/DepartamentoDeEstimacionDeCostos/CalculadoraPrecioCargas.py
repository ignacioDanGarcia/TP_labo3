from Cargas.Carga import Carga

class CalculadoraPrecioCargas():
    def __init__(self, contenedor):
        self.__contenedor = contenedor
        self.__cant_por_contenedor_lleno = None
        self.__cant_por_contenedor_no_lleno = None
        
    def calcular_precio_adicional_estado(self, carga: Carga):
        peso_carga = carga.get_peso()
        if peso_carga < 100:
            peso_carga = 100
        #Decidimos que si estás mandando 1 kg se te va a cobrar $1000 como si mandases 100kg, ponemos un minimo de cobro con la tabla de precios. 
        #Es 1000 cada 100 kg pero si no los aprovechas la empresa te cobra.
        medidas_int = self.get_contenedor().get_medidas_interior()
        if medidas_int.get_largo() == carga.get_medidas().get_largo() and medidas_int.get_ancho() == carga.get_medidas().get_ancho() and medidas_int.get_ancho() == carga.get_medidas().get_ancho():

            return self.get_cant_por_contenedor_lleno()
        elif medidas_int.comparar_medidas(carga.get_medidas()):
            
            return self.get_cant_por_contenedor_no_lleno() * (peso_carga // 100)
        else:
            return False

    def get_cant_por_contenedor_lleno(self):
        return self.__cant_por_contenedor_lleno
    def set_cant_por_contenedor_lleno(self, cant):
        self.__cant_por_contenedor_lleno = cant
    cant_por_contenedor_lleno = property(get_cant_por_contenedor_lleno,set_cant_por_contenedor_lleno)
    
    def get_cant_por_contenedor_no_lleno(self):
        return self.__cant_por_contenedor_no_lleno
    def set_cant_por_contenedor_no_lleno(self, cant):
        self.__cant_por_contenedor_no_lleno = cant
    cant_por_contenedor_no_lleno = property(get_cant_por_contenedor_no_lleno,set_cant_por_contenedor_no_lleno)

    def get_contenedor(self):
        return self.__contenedor
    def set_contenedor(self, cont):
        self.__contenedor = cont
    contenedor = property(get_contenedor,set_contenedor)