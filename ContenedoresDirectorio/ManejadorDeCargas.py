from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
class ManejadorDeCargas():
    def __init__(self) -> None:
        pass
    
    def verificar_carga(self, carga : Carga, contenedor):
        # este metodo la usa esta misma clase
        
        if "basico" in contenedor.tipo.lower() and carga.get_material_especial() != None: #En vez de que vea si es instancia de barco_basico_abstracto lo vemos por el tipo de barco
            return False

        if contenedor.medidas_interior.comparar_medidas(carga.get_medidas()) and \
                    carga.get_peso() <= contenedor.get_peso_max() and \
                    carga.get_volumen() <= contenedor.get_volumen_max():
                return True
        return False
    
    def cargar(self, carga :Carga, contenedor :Contenedor):
        if self.puede_cargar(carga, contenedor):
            contenedor.cargas.append(carga)
        return False
    def puede_cargar(self, carga:Carga, contenedor :Contenedor):
        return self.verificar_carga(carga,contenedor) # 