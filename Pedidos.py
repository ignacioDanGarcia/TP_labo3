class Pedidos:
    def __init__(self, retiraEnPuerto, conteneCompleto, id):
        self.__retiraEnPuerto = retiraEnPuerto #bool
        self.__conteneCompleto = conteneCompleto #bool
        self.__id = id
        'pruebas de git'
    
    'Getters y setters:'
    def get_retiraEnPuerto(self):
        return self.__retiraEnPuerto
    def set_retiraEnPuerto(self, ret):
        self.__retiraEnPuerto = ret
    retiraEnPuerto = property(get_retiraEnPuerto,set_retiraEnPuerto)

    def get_conteneCompleto(self):
        return self.__conteneCompleto
    def set_conteneCompleto(self, completo):
        self.__conteneCompleto = completo
    conteneCompleto = property(get_conteneCompleto,set_conteneCompleto)

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    id = property(get_id,set_id)