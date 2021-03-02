from models.Propuesta import Propuesta


class Escapada(Propuesta):
    def __init__(self, codigo, destino, fecha, descripcion, autobus):
        super().__init__(codigo, destino, fecha)
        self.__descripcion = descripcion
        self.__autobus = autobus
    def get_datos(self):
        super().get_datos()
        print("Descripcion: "+ self.__descripcion + " "+"Autobus: "+self.__autobus)
