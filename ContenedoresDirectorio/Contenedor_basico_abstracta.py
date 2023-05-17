from abc import ABC
from BarcosDirectorio.Excepciones.exceptions import el_contenedor_basico_no_puede_mat_especial
from Contenedores import Contenedor

class Cont_basico_abstracto(Contenedor, ABC):
    """
    VERIFICAR CARGA EN CLASE CONTENEDORES ABSTRACTA Y CONTENEDORES FLAT RACK QUEDA IGUAL
    EN ESTE TIPO DE CONTENEDORES SOLO HACE FALTA QUE RESPETE LAS MEDIDAS


    USO LA CLASE CONTENEDORES BASICO INTERFAZ PARA MODIFICARLA Y SOBREESCRIBIRLA
    PORQUE EN ESTE TIPO DE CONTENEDORES TAMBIEN HACE FALTA SABER SI ES O NO UN MATERIAL ESPECIAL
    Y SI ESE ES EL CASO NO PUEDE LLEVARSE LA CARGA

    """
    def verificar_carga(self, carga):
        super().verificar_carga(self, carga)
        if (carga.get_mat_especial() != None):
            raise el_contenedor_basico_no_puede_mat_especial("Un contenedor basico no puede cargar un material especial")
        return True