import uuid


class vuelo:

    def __nuevo__(self, destino: str, salida: float, plazas: int):
        self.id = str(uuid.uuid1().hex)
        self.destino = destino
        self.salida = salida
        self.plazas = plazas

    def __init__(self, id_json: str="", destino_json: str="", salida_json: float=0.0, plazas_json: int=0):
        self.id = id_json
        self.destino = destino_json
        self.salida = salida_json
        self.plazas = plazas_json

    def __str__(self):
        return f"{self.id}\n{self.destino}\n{self.salida}\n{self.plazas} \n"
