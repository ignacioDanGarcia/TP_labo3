class Barcos:
    def __init__(self, id, pesoMax, conteneMax):
        self.id = id
        self.disponible = True
        self.pesoMax = pesoMax
        self.conteneMax = conteneMax
        self.kmRecorrido = 0