from enum import Enum

class Categoria(Enum):
    MAQUINARIA = 1
    ALIMENTICIA = 2
    QUIMICA = 3
    
    #print(Categoria.ALIMENTICIA)  # Imprime: Categoria.ALIMENTICIA
    #print(Categoria.ALIMENTICIA.value)  # Imprime: 2