class Propuesta:
    def __init__(self, codigo, destino, fecha):
        self.__destino = destino
        self.__codigo = codigo
        self.__fecha = fecha

    def get_datos(self):
        print("Codigo: "+str(self.__codigo)+" Destino: " +
              self.__destino+" Fecha: "+self.__fecha)
