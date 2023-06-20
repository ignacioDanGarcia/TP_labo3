from ContenedoresDirectorio.Contenedores import Contenedor
class LocalizadorDeCargasConID():
    def __init__(self) -> None:
        pass
    
    def traer_cargas_del_id(self, id, contenedor :Contenedor):
        cargas_del_id = []
        for carga in contenedor.get_cargas():
            if carga.get_id() == id:
                cargas_del_id.append(carga)
        return cargas_del_id