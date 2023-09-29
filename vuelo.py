class vuelo:
    def __init__(self):
        pass

    def __init__(self, id_json:str, destino_json:str, salida_json:str, plazas_json:int):
        self.id = id_json
        self.destino = destino_json
        self.salida = salida_json
        self.plazas = plazas_json
        
    def __str__(self):
        return f"{self.id}\n{self.destino}\n{self.salida}\n{self.plazas} \n"            
    