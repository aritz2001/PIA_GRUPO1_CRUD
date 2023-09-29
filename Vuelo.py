import uuid
class Vuelo:
    def __init__(self):
        pass

    def __init__(self, destino, hora_salida, plazas_libres):
        self.id_vuelo = uuid.uuid1()
        self.destino = destino
        self.hora_salida
        self.plazas_libres