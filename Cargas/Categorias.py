from enum import Enum

class Categoria(Enum):
    ALIMENTICIA = 1
    QUIMICA = 2
    MAQUINARIA = 3
    
    #print(Categoria.ALIMENTICIA)  # Imprime: Categoria.ALIMENTICIA
    #print(Categoria.ALIMENTICIA.value)  # Imprime: 1