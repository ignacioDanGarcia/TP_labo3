from BarcosDirectorio.SistemasNavegacion.MetodosNavegacion import SistemaNavegacion


class AVela(SistemaNavegacion):
    def __init__(self, barco) -> None:
        super().__init__(barco)
        
    def navegar(self, horas):
        pass
        
    def mostrar_tipo(self):
        print("A vela")