import datetime
import uuid
import persistencia
import vuelo


lectura = persistencia.Persistencia()
lectura.cargar()
lectura.leer()

def menu():

    while True:
        try:
            opcion = int(input("¿Que desea hacer?\n 1-Leer el fichero \n 2-Crear un vuelo \n 3-Modificar un vuelo \n 4-Borrar un vuelo \n 0- Salir del programa \n "))
            match opcion:
                case 1:
                    atr = ""
                    valores = ""
                    lectura.leer()
                case 2:
                    year = int(input("Ingrese un año"))
                    month = int(input("Ingrese un mes"))
                    day = int(input("Ingrese un día"))
                    hour = int(input("Ingrese una hora"))
                    minute = int(input("Ingrese un minuto"))
                    salida = datetime.datetime(year, month, day, hour, minute, tzinfo=datetime.timezone.utc).timestamp()
                    destino = input("Ingrese el destino")
                    plazas = int(input("Ingrese la cantidad de plazas libres"))
                    lectura.crear_vuelo(destino,salida,plazas)

                case 3:
                    mi_uuid = input("Ingrese el uuid del vuelo a modificar")
                    atr = input("Ingrese el valor a modificar (destino,plazas_libres) ")
                    valores = input(f"Ingrese el nuevo valor a modificar {atr}: ")
                    lectura.modificar_vuelo(mi_uuid,atr,valores)
                case 4:
                    mi_uuid = input("Ingrese el uuid del vuelo a eliminar")
                    lectura.borrar_vuelo(mi_uuid)
                case 0:
                    print("Has salido de la aplicacion")
                    break
                case _:
                    print("Opción incorrecta")
        except ValueError:
            print("No se admiten valores de tipo string")
menu()
