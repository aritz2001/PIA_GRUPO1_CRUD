import uuid
import datetime

class vuelo:
    def __init__(self):
        pass

    def __init__(self, id_json:str, destino_json:str, salida_json:str, plazas_json:int):
        self.id = id_json
        self.destino = destino_json
        self.salida = salida_json
        self.plazas = plazas_json


    #def crear(self, destino:str, salida:datetime, plazas:int):
    #    self.id = uuid.uuid1()
    #    self.destino = destino
    #    self.salida = salida.datetime.timespan()
    #    self.plazas = plazas
        
    def __str__(self):
        return f"{self.id}\n{self.destino}\n{self.salida}\n{self.plazas} \n"            