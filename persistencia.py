
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

      def crear_vuelo(self,destino: str, salida: float, plazas: int):
            v=vuelo.vuelo()
            v.__nuevo__(destino, salida, plazas)          
            self.datos.append(v)
            print("Insertando ...")
            self.guardar()
            print("Insertado con éxito")


      def modificar_vuelo(self,mi_uuid,atr,valor):
        for vuelo in self.datos:
          if vuelo.id == mi_uuid:
              if atr == "destino":
                  print(atr,"Antes de Modificarlo:", vuelo.destino)
                  vuelo.destino = valor
                  print(atr,"Despues de Modificarlo:", vuelo.destino)
              else:
                print(atr,"Antes de Modificarlo:", vuelo.plazas)
                vuelo.destino = valor
                print(atr,"Despues de Modificarlo:", vuelo.plazas)
                
        print("Modificando ...")
        self.guardar()
        print("Modificado con éxito")
    
      def borrar_vuelo(self ,mi_uuid):
        for vuelo in self.datos:
          if vuelo.id == mi_uuid:
              self.datos.remove(vuelo)
        print("Borrando ...")
        self.guardar()
        print("Borrado con éxito.")
             

              
            
        