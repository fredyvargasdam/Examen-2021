from models.Propuesta import Propuesta


class Viaje(Propuesta):
    def __init__(self, codigo, destino, fecha, fecha_fin, tur_operadora, vuelo_ida, vuelo_vuelta):
        super().__init__(codigo, destino, fecha)
        self.__fecha_fin = fecha_fin
        self.__tur_operadora = tur_operadora
        self.__vuelo_ida = vuelo_ida
        self.__vuelo_vuelta = vuelo_vuelta
