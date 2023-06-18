from BarcosDirectorio.SistemasNavegacion.MetodosNavegacion import SistemaNavegacion
class AMotor(SistemaNavegacion):
    def __init__(self, barco) -> None:
        super().__init__(barco)
    
    def navegar(self, horas):
        gasto_total = horas * self.barco.get_gasto_por_hora()
        combustible_actual = self.barco.get_combustible_actual()
        self.barco.set_combustible_gastado(self.barco.get_combustible_gastado() + gasto_total)
        self.barco.set_combustible_actual(combustible_actual - gasto_total)
    
    def mostrar_tipo(self):
        print("A motor")