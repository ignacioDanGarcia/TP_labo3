import random
"""
Llegamos a la conclusion de que debería ser otro objeto especifico que se encargue
de settear un precio de una carga, para cumplir con el principio de responsabilidad
unica.

Siguiendo una logic acoherente, para saber el valor de un objeto, habria que ponernos
a analizar muchas caracteristicas como las medidas, valor social y demas. Las medidas
estan contempladas en la tabla de precios, de lo cual se encarga el contenedor.
Ahora, esta clase la creamos, porque necesitabamos un ente, un objeto, que decida
el costo verdadero de una carga en si. Capaz este ente considera que llevar una coca
de 250 ml, cuesta mil veces mas que llevar un delorean maquina del tiempo con 30 
valijas llenas de plutonio pero bueno, es puro juicio de esta clase.

Por eso pusimos que devuelva un numero random.
"""


class Tasador_de_cargas():
    def setear_precio_carga(self):
        return random.randint(1, 20000)