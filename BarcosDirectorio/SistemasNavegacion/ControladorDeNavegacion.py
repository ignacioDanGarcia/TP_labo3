from BarcosDirectorio.SistemasNavegacion.AMotor import AMotor
from BarcosDirectorio.SistemasNavegacion.AVela import AVela

class ControladorDeSistemaDeNavegacion():
    def __init__(self) -> None:
        pass
    
    def optimizar_navegacion(self, barco, vientoFavorable):
        if vientoFavorable:
            sistema_a_vela = AVela(barco)
            barco.set_sistema_navegacion(sistema_a_vela)
            
        elif barco.get_sistema_navegacion() != AMotor:
            sistema_a_motor = AMotor(barco)
            barco.set_sistema_navegacion(sistema_a_motor)
    
    