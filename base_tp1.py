"""""
Este código ha sido desarrollado por el grupo 136
"""
import random

# Título, mensaje de bienvenida y reglas
titulo = """
+++++++++++++++++
+  El Juego de  +
+  Dos o Tres   +
+++++++++++++++++
"""

print(titulo)
reglamento = """
El juego de 2 o 3 requiere a dos jugadores, se juega con tres dados y dura dos rondas.

En la primera ronda cada jugador tirará sus tres dados. Si hay 3 dados iguales, el jugador suma 6 puntos.
Si hay dos dados iguales el jugador suma 3 puntos y tiene la posibilidad de relanzar el dado distinto para sumar 
otros 3 puntos si logra igualar a los demás dados. Si no hay dados iguales, entonces el jugador no suma ningún punto.

En la segunda ronda cada jugador debe realizar una apuesta por par o impar y luego tirar sus 3 dados.
Si la suma de los dados es de la paridad apostada, el jugador sumara una cantidad de puntos igual al dado de mayor
valor obtenido. Si además todos los dados resultan de la paridad apostada, se duplicará su puntaje.
Si en cambio, la suma de los dados no es de la paridad elegida, entonces el jugador perderá puntaje igual
al dado de menor valor.

Gana el juego aquel jugador que obtenga la mayor cantidad de puntos!"""

reglas = input("Bienvenido! ¿Desea leer las reglas del juego antes de empezar? (S/N)\n")
if reglas == "s" or reglas == "S":
    print(reglamento)

# Carga de nombre de jugadores y comienzo del juego
jugador1 = input("Jugador 1, ingrese su nombre: ")
jugador2 = input("Jugador 2, ingrese su nombre: ")
input("\nEl juego está listo. Presione Enter para comenzar")
puntaje1, puntaje2 = 0, 0

# PRIMERA RONDA
print("-"*60)
print("INICIO RONDA 1")

# Jugador 1
print("-"*60)
input("Turno de {}: presione enter para lanzar los dados...".format(jugador1))
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 1 primera ronda
relanzar, comparar = False, None
if dado1 == dado2 and dado1 == dado3:
    puntaje1 += 6
    print(jugador1, "obtiene 6 puntos")
elif dado1 == dado2:
    puntaje1 += 3
    relanzar = True
    comparar = dado1
elif dado1 == dado3:
    puntaje1 += 3
    relanzar = True
    comparar = dado1
elif dado2 == dado3:
    puntaje1 += 3
    relanzar = True
    comparar = dado2

if relanzar:
    print("Tienes dos dados iguales, obtienes 3 puntos.")
    input("Presiona enter para volver a tirar el dado distinto: ")
    dado4 = random.randint(1, 6)
    print("Tu dado salió: [{}]".format(dado4))
    if dado4 == comparar:
        print("Sumas 3 puntos más!")
        puntaje1 += 3

print("\nFin de la jugada. En esta ronda", jugador1, "obtuvo", puntaje1, "puntos.")

# Jugador 2
print("-"*60)
input("Turno de {}: presione enter para lanzar los dados...".format(jugador2))
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 2 primera ronda
relanzar, comparar = False, None
if dado1 == dado2 and dado1 == dado3:
    puntaje2 += 6
    print(jugador2, "obtiene 6 puntos")
elif dado1 == dado2:
    puntaje2 += 3
    relanzar = True
    comparar = dado1
elif dado1 == dado3:
    puntaje2 += 3
    relanzar = True
    comparar = dado1
elif dado2 == dado3:
    puntaje2 += 3
    relanzar = True
    comparar = dado2

if relanzar:
    print("Tienes dos dados iguales, obtienes 3 puntos.")
    input("\nPresiona enter para volver a tirar el dado distinto: ")
    dado4 = random.randint(1, 6)
    print("Tu dado salió: [{}]".format(dado4))
    if dado4 == comparar:
        print("Sumas 3 puntos más!")
        puntaje2 += 3


print("\nFin de la jugada. En esta ronda", jugador2, "obtuvo", puntaje2, "puntos.")

# Puntajes parciales
print("-"*60)
print("Puntajes Parciales: ", jugador1, "tiene", puntaje1, "puntos y", jugador2, "tiene", puntaje2, "puntos")
input("Presione enter para pasar a la Segunda Ronda")

# Segunda Ronda
print("\n"+"-"*60)
print("INICIO SEGUNDA RONDA")

# Jugador1
print("-"*60)
print("Turno de {}".format(jugador1))

# Apuesta jugador 1
print("Debe apostar por resultado par o impar.")
apuesta1 = input("¿Desea apostar por par? (s/n)\n")
if apuesta1 == "s" or apuesta1 == "S":
    apuesta1 = 0
    print(jugador1, "apuesta por par...")
elif apuesta1 == "n" or apuesta1 == "N":
    apuesta1 = 1
    print(jugador1, "apuesta por impar...")
else:
    apuesta1 = 1
    print("No se entendió su apuesta. Por defecto", jugador1, "apuesta por impar...")

print("-"*60)
input("Presione enter para lanzar los dados...")
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 1 Segunda Ronda
mayor1 = max(dado1, dado2, dado3)
menor1 = min(dado1, dado2, dado3)
suma1 = dado1 + dado2 + dado3
if suma1 % 2 == 0:
    print("\nLa suma de los dados es par!")
else:
    print("\nLa suma de los dados es impar!")
if suma1 % 2 == apuesta1:
    puntaje1 += mayor1
    print(jugador1, "obtiene", mayor1, "puntos")
    if dado1 % 2 == apuesta1 and dado2 % 2 == apuesta1 and dado3 % 2 == apuesta1:
        print("Todos los dados coinciden con la apuesta!", jugador1, "duplica su puntaje!!!")
        puntaje1 *= 2
        print(jugador1, "ahora tiene", puntaje1, "puntos")
else:
    puntaje1 -= menor1
    print(jugador1, "pierde", menor1, "puntos")

# Jugador2
print("-"*60)
print("Turno de {}".format(jugador2))

# Apuesta jugador 2
print("Debe apostar por resultado par o impar.")
apuesta2 = input("¿Desea apostar por par? (s/n)\n")
if apuesta2 == "s" or apuesta2 == "S":
    apuesta2 = 0
    print(jugador2, "apuesta por par...")
elif apuesta2 == "n" or apuesta2 == "N":
    apuesta2 = 1
    print(jugador2, "apuesta por impar...")
else:
    apuesta2 = 1
    print("No se entendió su apuesta. Por defecto", jugador2, "apuesta por impar...")

print("-"*60)
input("Presione enter para lanzar los dados...")
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 1 Segunda Ronda
mayor2 = max(dado1, dado2, dado3)
menor2 = min(dado1, dado2, dado3)
suma2 = dado1 + dado2 + dado3
if suma2 % 2 == 0:
    print("\nLa suma de los dados es par!")
else:
    print("\nLa suma de los dados es impar!")
if suma2 % 2 == apuesta2:
    puntaje2 += mayor2
    print(jugador2, "obtiene", mayor2, "puntos")
    if dado1 % 2 == apuesta2 and dado2 % 2 == apuesta2 and dado3 % 2 == apuesta2:
        print("Todos los dados coinciden con la apuesta!", jugador2, "duplica su puntaje!!!")
        puntaje2 *= 2
        print(jugador2, "ahora tiene", puntaje2, "puntos")
else:
    puntaje2 -= menor2
    print(jugador2, "pierde", menor2, "puntos")

# Resultado
print("="*60)
print("FIN DE LA PARTIDA")
print("="*60)
input("\nVeamos quien ganó... Presione enter para continuar...\n")
print("*"*60)
print("*", jugador1, "obtuvo", puntaje1, "puntos y", jugador2, "obtuvo", puntaje2, "puntos")
if puntaje1 == puntaje2:
    print("* El resultado es empate! :/")
elif puntaje1 > puntaje2:
    print("* El ganador es", jugador1, "!!!")
else:
    print("* El ganador es", jugador2, "!!!")
print("*"*60)
print("\nGracias por jugar!\nEsperamos que lo hayan disfrutado :D")

# Créditos
creditos = """
(lease con voz en off...)

Diseño: Equipo docente
    -ing. Romina Teicher
    -ing. Marcela Tartabini
    -ing. Jorge Harach

Ejecución: Grupo 136 
    -Matías Avila (93599)
    -Nathaniel Balderramas (92334)
    -Gabriela Silva (92708)
"""
input("Presione enter para ver los créditos del juego...")
print(creditos)
