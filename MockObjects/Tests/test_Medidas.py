from unittest import TestCase

from pytest import raises
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas

class TestMedidas(TestCase):
    def test_calcular_volumen_con_numeros_de_variables_de_medidas_bajos_e_iguales(self):
        medidas = Medidas(3,3,3)
        carga = Carga(medidas,3,Categoria.MAQUINARIA)
        assert(carga.get_volumen()) == 27
        
    def test_calcular_volumen_con_numeros_de_variables_de_medidas_medianos_y_distintos(self):
        medidas = Medidas(8,5,2)
        carga = Carga(medidas,3,Categoria.MAQUINARIA)
        assert(carga.get_volumen()) == 80
    
    
    def test_metodo_comparar_medidas_de_clase_medidas_tira_false_por_medidas_mas_altas_que_self(self):
         #devuelve FAlSE si las medidas pasadas por parametro son mayores a las de la instancia
        #devuelve TRUE si las medidas pasadas x parametro son menores o iguales a las de la instancia
        medidas_1 = Medidas(3,3,3)
        medidas_2 = Medidas(4,4,3)
        
        assert  medidas_1.comparar_medidas(medidas_2) == False

    def test_metodo_comparar_medidas_de_clase_medidas_tira_true_por_medidas_mas_bajas_que_self(self):
         #devuelve FAlSE si las medidas pasadas por parametro son mayores a las de la instancia
        #devuelve TRUE si las medidas pasadas x parametro son menores o iguales a las de la instancia
        medidas_2 = Medidas(3,3,3)
        medidas_1 = Medidas(4,4,3)
        
        assert(medidas_1.comparar_medidas(medidas_2)) == True
        