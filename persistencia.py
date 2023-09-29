
import json
import Vuelo

class Persistencia:
    
      def __init__(self):
        self.datos: list[] = []
        
      def cargar(self):
        with open('./bbdd.json') as file:
            temp = json.load(file)
            f#or x in temp:
              #  self.data.append(Vuelo(x['artist'], x['name'], int(x['year'])))

      def guardar(self):
        temp = json.dumps([ob.__dict__ for ob in self.datos], indent=4)

        with open("./bbdd.json", "w", encoding='utf8') as outfile:
            outfile.write(temp)
    