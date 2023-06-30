def validaNumRango(tipo,mensajeIngreso,rmin,rmax):
    while True:
        try:
            num = tipo(input(mensajeIngreso))
            if rmin!=None and rmax!=None:
                if rmin<=num<=rmax:
                    break
                else:
                    print(f"Inválido. Ingresar número entre el rango de {rmin} y {rmax}")
            elif rmin!=None:
                if rmin<=num:
                    break
                else:
                    print("Rango mínimo debe ser MENOR o IGUAL a número ingresado.")
            elif rmax!=None:
                if rmax>=num:
                    break
                else:
                    print("Rango máximo debe ser MAYOR o IGUAL a número ingresado.")
        except:
            print("Inválido. Ingrese un NÚMERO.")
    return num

def validaNum(tipo,mensajeIngreso):
    while True:
        try:
            num = tipo(input(mensajeIngreso))
        except:
            print("Inválido. Ingrese un NÚMERO.")
        else:
            break
    return num

def validaLetras(mensajeIngreso):
    while True:
        try:
            palabra=input(mensajeIngreso)
            if palabra.isalpha():
                break
            else:
                print("Inválido. Ingrese SOLO LETRAS.")
        except:
            print("Inválido.")
    return palabra

def validaSN(mensajeIngreso):
    while True:
        try:
            sn = validaLetras(mensajeIngreso)
            sn = sn.lower()
            if sn!='s' or sn!='n':
                print("Opción SOLO debe ser 's' o 'n'.")
            else:
                break
        except:
            print("Inválido")

def menuPrincipal(nombre,apellido):
    print("-"*20,f"¡Bienvenid@, {nombre} {apellido}!","-"*20)
    print("1. Guardar datos Jugador")
    print("2. Buscar Jugador por RUT")
    print("3. Imprimir Parejas")
    print("4. Salir")

def validaNombre():
        while True:
            try:
                nombre = validaLetras("Ingrese el nombre del jugador: ")
                if len(nombre)<2:
                    print("Nombre debe tener MÁS de dos cáracteres")
                else:
                    break
            except:
                print("Inválido")
        return nombre

def validaNombrePareja():
        while True:
            try:
                nombre = validaLetras("Ingrese el nombre de la pareja del Jugador: ")
                if len(nombre)<2:
                    print("Nombre debe tener MÁS de dos cáracteres")
                else:
                    break
            except:
                print("Inválido")
        return nombre

def validaAño():
    while True:
        try:
            fechaNac = validaNum(int,"Ingrese su año de nacimiento: ")
            if 2023-fechaNac>80:
                print("Persona ingresada NO debe tener MÁS de 80 años.")
            else:
                break
        except:
                print("Inválido")
    return fechaNac

def validaCorreo():
    while True:
        try:
            correo = input("Ingrese el correo: ")
            if correo.count('@')!=1:
                print("Correo DEBE tener carácter '@'")
            elif len(correo)<6:
                print("Largo mínimo de correo debe ser MAYOR a 6 carácteres")
            else:
                break
        except:
            print("Inválido.")
    return correo

def menuCategoria():
    print("Seleccione la categoría correspondiente: ")
    print("1. Oro")
    print("2. Plata")
    print("3. Bronce")
    opc = validaNumRango(int,"\n> ",1,3)
    if opc==1:
        categoria = 'Oro'
    elif opc==2:
        categoria = 'Plata'
    else:
        categoria = 'Bronce'
    return categoria


#def guardarJugador(nombre,fechaNac,categoria,celular):

