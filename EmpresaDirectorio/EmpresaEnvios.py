from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import CombustibleInsuficienteException, tiempo_incorrecto
"""
CLASE QUE HACE VIAJAR A LOS VEHICULOS
"""

class EmpresaEnvios():
    def __init__(self, empresa_data : EmpresaData) -> None:
        self.administracion_empresaData = empresa_data
    
        """
        recibe los barcos o camiones llenos y los hace "viajar"
        o los pone en modo viajando que seria disponible = False
        """
    def hacer_viajar_barcos(self, barcos, gps):
        for barco in barcos:
            try:
                barco.puede_navegar(gps) # este metodo lanza excepcion
                barco.navegar(gps)
            except CombustibleInsuficienteException as e:
                print(e.mensaje)

                    

    def descargar_cargas_contenedores_barcos(self, barcos):
        #lista_con_todos_los_contenedores = []

        #este for setea todas las cargas de los contenedores de cada barco en None
        for barco in barcos:

            lista_contenedores_aux = []

            for contenedor in barco.get_contenedores():
                contenedor.set_cargas(None)
                contenedor.set_precio_transporte_base(0)#seteo contadores del contenedor en cero
                contenedor.set_cant_de_veces_comple_y_carga_unica(0)
                lista_contenedores_aux.append(contenedor)
                #lista_con_todos_los_contenedores.append(contenedor)
    
            barco.set_lista_contenedores(lista_contenedores_aux)
            barco.set_disponible(True)
            barco.set_combustible_gastado(0)
            barco.set_km_recorridos(0)

        #esto actualiza los datos de la empresa
        #aca sirve usar un Singleton para EmpresaData que es la que tiene la lista de contenedores
        #self.administracion_empresaData.set_barcos(barcos)
        #self.administracion_empresaData.set_contenedores(lista_con_todos_los_contenedores)
       
    def hacer_viajar_camiones(self,camiones):
        for camion in camiones:
            camion.viajar()
    
    def descargar_cargas_contenedores_camiones(self, camiones):
        for camion in camiones:
            cont_aux = camion.get_contenedor()

            cont_aux.set_cargas(None)  #seteo contadores y cargas del contenedor en cero
            cont_aux.set_cant_de_veces_comple_y_carga_unica(0)
            cont_aux.set_precio_transporte_base(0)
            #camion.get_contenedor().set_cargas(None)\
            #.set_cant_de_veces_comple_y_carga_unica(0)\
            #.set_precio_transporte_base(0)
            camion.set_contenedor(cont_aux) #le cambio al camion el contenedor



            

