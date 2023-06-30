import funciones as fn
import numpy as np

# jugador = [nombre, rut, añoNac, categoria, celular, pareja, correo]
#              0      1      2        3         4       5        6
# crear nuevo arreglo/lista cada vez que se ingresa a la opc 1

#jugadores = [lista_jugador1], [lista_jugador2]...
opc = 0
contJugador= 0
tamaño = fn.validaNum(int,"Ingrese la cantidad de jugadores que desea agregar: ")
jugadores = np.zeros((tamaño), type(int))
nombreCliente = fn.validaLetras("Ingrese su nombre: ").capitalize()
apellidoCliente = fn.validaLetras("Ingrese su apellido: ").capitalize()
while opc!=4:
    fn.menuPrincipal(nombreCliente,apellidoCliente)
    opc = fn.validaNumRango(int,"Ingrese la opción deseada:\n> ",1,4)
    if opc==1:
        cont=''
        while contJugador<tamaño:
            for i in range(len(jugadores)):
                contJugador+=1
                jugador = []
                print("-"*20,f"JUGADOR #{contJugador}","-"*20)
                nombre = fn.validaNombre().capitalize()
                rut = fn.validaNum(int,"Ingrese su RUT: ")
                fechaNac = fn.validaAño()
                categoria = fn.menuCategoria()
                celular = fn.validaNum(int,"Ingrese su celular: ")
                pareja = fn.validaNombrePareja().capitalize()
                correo = fn.validaCorreo()
                jugador.append(nombre)
                jugador.append(rut)
                jugador.append(fechaNac)
                jugador.append(categoria)
                jugador.append(celular)
                jugador.append(pareja)
                jugador.append(correo)
                input(f"Los datos del jugador se resumen en los siguientes:\n{jugador} ...")
                jugadores[i] = jugador
                break
        else:
            print("Cantidad de jugadores máxima alcanzada.")
    elif opc==2:
        buscarRUT = fn.validaNum(int,"Ingrese el RUT del Jugador que desea buscar:\n> ")
        buscarRut = str(buscarRUT)
        for i in range(len(jugadores)):
            if buscarRut in jugadores[i]: # al menos aparece una vez (ÓSEA, SI ESTÁ)
                print("¡JUGADOR ENCONTRADO!")
                print(f"Nombre: {jugadores[i][0]}")
                print(f"Categoria: {jugadores[i][3]}")
                print(f"Fono: {jugadores[i][4]}")
                print(f"Correo: {jugadores[i][6]}")
            else:
                print("Jugador NO encontrado.")
    elif opc==3:
        buscarPareja = fn.validaLetras(int,"Ingrese el nombre de la pareja que pertenezca al equipo que desea buscar:\n> ")
        buscarPareja = str(buscarPareja)
        for i in range(len(jugadores)):
            if buscarPareja in jugadores[i]:
                print("¡PAREJA ENCONTRADA!")
                print(f"Nombre integrante: {jugadores[i][0]}")
            else:
                print("Pareja NO encontrada.")
    else:
        print(f"¡Nos vemos, {nombreCliente} {apellidoCliente}!")
