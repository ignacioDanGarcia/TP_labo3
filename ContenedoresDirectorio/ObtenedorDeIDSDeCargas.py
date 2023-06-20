from ContenedoresDirectorio.Contenedores import Contenedor
class ObtenedorIDSCargas():
    def __init__(self):
        pass
    
    def obtener_ids_cargas(self, contenedor :Contenedor):
        ids_cargas = set()
        for carga in contenedor.get_cargas():
            ids_cargas.add(carga.get_id())
        return list(ids_cargas)