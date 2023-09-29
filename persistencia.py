
import json
import vuelo

class Persistencia:
    
      def __init__(self):
        self.datos: list[vuelo.vuelo] = []         
        
      def leer(self):
          for x in self.datos:
           print(x.__str__())

        
      def cargar(self):
        with open('./bbdd.json') as file:
            temp = json.load(file)
            for x in temp:
                self.datos.append(vuelo.vuelo(x['id'], x['destino'], x['salida'], x['plazas']))

      def guardar(self):
        temp = json.dumps([ob.__dict__ for ob in self.datos], indent=4)

        with open("./bbdd.json", "w", encoding='utf8') as outfile:
            outfile.write(temp)
    