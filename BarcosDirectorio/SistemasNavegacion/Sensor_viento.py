from BarcosDirectorio.SistemasNavegacion.AVela import AVela
from BarcosDirectorio.SistemasNavegacion.AMotor import AMotor
from BarcosDirectorio.SistemasNavegacion.ControladorDeNavegacion import ControladorDeSistemaDeNavegacion
import random
import time
class SensorViento():

    def __init__(self) -> None:
        self.controlador = ControladorDeSistemaDeNavegacion() #El controlador de navegacion
    
    def medir_viento_favorable(self, barco):
        numero_aleatorio = random.randint(1, 10)
        print(f"Numero aleatorio: {numero_aleatorio}")
        if numero_aleatorio >3 :
            self.notify(barco,True) 
            return True
        #Logica que decide si el viento es favorable para usar las velas. Acá hay mas chances de que sea favorable a que no
        self.notify(barco,False) 
        return False
        #Si el viento no es favorable le notifico al sistema de navegacion para que optimice la navegacion. Si es favorable le notifico que si
    
  
    
    def notify(self,barco, vientoFavorable):
        self.controlador.optimizar_navegacion(barco,vientoFavorable)
        