#Introducción a la programación Seccción 17
#Fecha de creación del programa: 13/11/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Crear un juego de Batalla Naval en Python para dos jugadores, donde puedan colocar estratégicamente sus barcos en un tablero y, por turnos, intentar adivinar la ubicación de los barcos del oponente. 

from typing import List
class Casilla:
    def __init__(self):
        self.espacio_disp = "   |"
        self.coordenada_x = 0
        self.coordenada_y = 0
        self.estado = 1

class Barco:
    def __init__(self):
        self.casilla_inicial_x = 3
        self.casilla_inicial_y = 3
        self.posicion = 1
        self.numero_casillas = 5
        self.nombre = "Porta_Aviones"
        self.area = []

class Jugador:
    def __init__(self):
        self.flota = []
        self.tablero = []
        self.ataque = []

class Tiro:
    def __init__(self):
        self.coordenadas = Casilla()
        self.resultado = 0

def validar_int(msj):
    while True:
        try:
            valor = int(input(msj))
            if 1 <= valor <= 10:
                return valor
            else:
                print("El dato ingresado no es válido, debe ser un número entero entre 1 y 10:")
        except ValueError:
            print("El dato ingresado no es válido, debe ser un número entero entre 1 y 10:")

def validar_int_pos(msj):
    while True:
        try:
            valor = int(input(msj))
            if valor in [0, 1]:
                return valor
            else:
                print("El dato ingresado no es válido, debe ser 0 o 1:")
        except ValueError:
            print("El dato ingresado no es válido, debe ser 0 o 1:")

def validar_str(msj):
    while True:
        valor = input(msj).upper()
        if "A" <= valor <= "J" and len(valor) == 1:
            return ord(valor) - 65
        else:
            print("El dato ingresado no es válido, debe ser una letra de la A a la J:")

def dibujar_cuadricula(casilla_list):
    agua2 = "___|"

    for i in range(10):
        print(f"   {i + 1}", end=" ")

    print("\n  ", end=" ")
    for i in range(10):
        print("___ ", end=" ")

    for valor in range(65, 75):
        letra = chr(valor)
        print(f"\n{letra}|", end=" ")
        for i in range(1, 11):
            espacio = False
            for casilla in casilla_list:
                if casilla.coordenada_y == (valor - 65) and casilla.coordenada_x == i:
                    print(casilla.espacio_disp, end="")
                    espacio = True
                    break
            if not espacio:
                print("   |", end=" ")

    print()

def dibujar_tiro(tiro, casilla_list2):
    print("Dibujando...")
    casilla_list = []

    if tiro.resultado == 1:
        print("¡Tiro acertado!")
        casilla = Casilla()
        casilla.coordenada_x = tiro.coordenadas.coordenada_x
        casilla.coordenada_y = tiro.coordenadas.coordenada_y
        casilla.espacio_disp = " x |"
        casilla.estado = 2

        casilla_list.append(casilla)

    elif tiro.resultado == 0:
        print("Tiro fallido")
        casilla1 = Casilla()
        casilla1.coordenada_x = tiro.coordenadas.coordenada_x
        casilla1.coordenada_y = tiro.coordenadas.coordenada_y
        casilla1.espacio_disp = " - |"
        casilla1.estado = 3

        casilla_list.append(casilla1)

    elif tiro.resultado == 2:
        print("¡Hundiste un barco!")
        casilla2 = Casilla()
        casilla2.coordenada_x = tiro.coordenadas.coordenada_x
        casilla2.coordenada_y = tiro.coordenadas.coordenada_y
        casilla2.espacio_disp = " @ |"
        casilla2.estado = 4

        casilla_list.append(casilla2)

    print(len(casilla_list))
    return casilla_list

def resultado_tiro(tiro, jugador, jugador_oponente):
    res = 0
    tiros_barco = []

    for tiro1 in jugador.ataque:
        tiros_barco.append(tiro1.coordenadas)

    for casilla_barco in jugador_oponente.flota:
        if any(casilla.coordenada_x == tiro.coordenadas.coordenada_x and casilla.coordenada_y == tiro.coordenadas.coordenada_y for casilla in casilla_barco.area):
            tiros_barco.append(tiro.coordenadas)
            if len(casilla_barco.area) - len(list(filter(lambda x: x in tiros_barco, casilla_barco.area))) == 0:
                res = 2
            else:
                res = 1

    tiro.resultado = res
    return tiro

def dibujar_barco(barco, casilla_list2):
    casilla_list = []

    if barco.posicion == 0:
        for y in range(barco.casilla_inicial_y, barco.casilla_inicial_y + barco.numero_casillas):
            casilla = Casilla()
            casilla.coordenada_x = barco.casilla_inicial_x
            casilla.coordenada_y = y
            casilla.espacio_disp = " B |"
            casilla.estado = 1

            casilla_list.append(casilla)
    else:
        for x in range(barco.casilla_inicial_x, barco.casilla_inicial_x + barco.numero_casillas):
            casilla = Casilla()
            casilla.coordenada_y = barco.casilla_inicial_y
            casilla.coordenada_x = x
            casilla.espacio_disp = " B |"
            casilla.estado = 1

            casilla_list.append(casilla)

    duplicates = [item for item in casilla_list2 if item in casilla_list]

    for lista in duplicates:
        print(any(duplicates))

    if duplicates:
        print("Impactarás con otro barco, ingresa nuevas coordenadas:")
        return solicitar_coordenadas(barco.nombre, casilla_list2)
    else:
        barco.area.extend(casilla_list)
        return barco

def solicitar_coordenadas(nombre, casilla_list2):
    barco = Barco()
    print("for dentro")

    if nombre == "Acorazado":
        barco.nombre = nombre
        barco.numero_casillas = 4
    elif nombre == "PortaAviones":
        barco.nombre = nombre
        barco.numero_casillas = 5
    elif nombre == "Crucero":
        barco.nombre = nombre
        barco.numero_casillas = 1
    elif nombre == "Submarino":
        barco.nombre = nombre
        barco.numero_casillas = 3
    elif nombre == "Destructor":
        barco.nombre = nombre
        barco.numero_casillas = 2

    casilla_list = []

    barco.nombre = nombre

    print(f"\n\n{barco.nombre.upper()}: {barco.numero_casillas} casillas\n\n")

    barco.posicion = validar_int_pos("Ingrese 0 si su barco estará en vertical, o si estará en horizontal ingrese 1:")
    barco.casilla_inicial_x = validar_int("Ingrese una coordenada numérica en la que iniciará las dimensiones de su barco del 1 al 10:")
    barco.casilla_inicial_y = validar_str("Ingrese una coordenada alfanumérica en la que iniciará las dimensiones de su barco, de la A a la J:") - 65

    while (barco.casilla_inicial_x + barco.numero_casillas > 10 and barco.posicion == 1) or (barco.casilla_inicial_y + barco.numero_casillas > 10 and barco.posicion == 0):
        barco.casilla_inicial_x = validar_int("La coordenada numérica en la que iniciará las dimensiones de su barco del 1 al 10 no estan disponibles en las casillas")
        barco.casilla_inicial_y = validar_str("Ingrese una coordenada alfanumérica en la que iniciará las dimensiones de su barco, de la A a la J:") - 65

    barco = dibujar_barco(barco, casilla_list2)

    return barco

def cambiar_espacio(estado):
    mi_casilla = Casilla()

    if estado == 0:
        mi_casilla.espacio_disp = "   |"
    elif estado == 1:
        mi_casilla.espacio_disp = " B |"
    elif estado == 2:
        mi_casilla.espacio_disp = " X |"
    else:
        mi_casilla.espacio_disp = " - |"

def solicitar_tiro(jugador_oponente, jugador):
    tiro = Tiro()
    casilla_list = []

    print("\n\n Elije la casilla a la que enviara el tiro y escribe las coordenadas \n\n")

    tiro.coordenadas.coordenada_x = validar_int("Ingrese coordenada numérica X")
    tiro.coordenadas.coordenada_y = validar_str("Ingrese coordenada alfanumérica Y") - 65

    while any(casilla.coordenada_x == tiro.coordenadas.coordenada_x and casilla.coordenada_y == tiro.coordenadas.coordenada_y for casilla in jugador.tablero):
        print("Ya ingreso esta coordenada, por favor ingrese una diferente ")
        tiro.coordenadas.coordenada_x = validar_int("Ingrese coordenada numérica X")
        tiro.coordenadas.coordenada_y = validar_str("Ingrese coordenada alfanumérica Y") - 65

    print(f"X{tiro.coordenadas.coordenada_x}")
    print(f"Y{tiro.coordenadas.coordenada_y}")

    tiro.resultado = resultado_tiro(tiro, jugador, jugador_oponente).resultado

    casilla_list.extend(dibujar_tiro(tiro, casilla_list))

    jugador.ataque.append(tiro)
    jugador.tablero.extend(casilla_list)

    return jugador

def main():
    jugador1 = Jugador()
    jugador2 = Jugador()

    print('BATALLA NAVAL')
    nombre_barcos = ["Porta Aviones", "Acorazado", "Crucero", "Submarino", "Destructor"]

    casilla_list_tiro1 = []
    casilla_list_tiro2 = []
    casilla_list_flota1 = []
    casilla_list_flota2 = []

    ataque_jugador1 = []
    ataque_jugador2 = []

    jugador1 = Jugador()
    jugador2 = Jugador()

    print('Jugador 1')

    for i in range(5):
        if len(jugador1.flota) < 1:
            print("for antes")
            jugador1.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota1))
        else:
            jugador1.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota1))
        casilla_list_flota1.extend(jugador1.flota[i].area)
        dibujar_cuadricula(casilla_list_flota1)

    input("Presione cualquier letra para continuar")

    print('Jugador 2')

    for i in range(5):
        if len(jugador2.flota) < 1:
            jugador2.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota2))
        else:
            jugador2.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota2))
        casilla_list_flota2.extend(jugador2.flota[i].area)
        dibujar_cuadricula(casilla_list_flota2)

    input("Presione cualquier letra para continuar")

    print('INICIA EL JUEGO')

    while True:
        print('TURNO JUGADOR 1')

        jugador1 = solicitar_tiro(jugador2, jugador1)
        dibujar_cuadricula(jugador1.tablero)
        input("Presione cualquier letra para continuar")

        print('TURNO JUGADOR 2')

        jugador2 = solicitar_tiro(jugador1, jugador2)
        dibujar_cuadricula(jugador2.tablero)
        input("Presione cualquier letra para continuar")

        if jugador1.ataque.count(lambda tiro: tiro.resultado == 1) >= 15 or jugador2.ataque.count(lambda tiro: tiro.resultado == 1) >= 15:
            break

    if jugador1.ataque.count(lambda tiro: tiro.resultado == 1) > jugador1.ataque.count(lambda tiro: tiro.resultado == 1):
        print('GANA JUGADOR 1')
    else:
        print('GANA JUGADOR 2')

if __name__ == "__main__":
    main()