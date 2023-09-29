
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
      def modificar_vuelo(self,mi_uuid,atr,valor):  
        for vuelo in self.datos:
          if vuelo.id == mi_uuid:
              if atr == "destino":
                  vuelo.destino = valor
                  print(atr,"Antes de Modificarlo:", vuelo.destino)
              else:
                vuelo.salida = valor
                print(atr,"Despues de Modificarlo:", vuelo.salida)
        self.guardar()
        
    
      def borrar_vuelo(self ,mi_uuid):
        for vuelo in self.datos:
          if vuelo.id == mi_uuid:
              self.datos.remove(vuelo)
              
        self.guardar()
             

              
            
        