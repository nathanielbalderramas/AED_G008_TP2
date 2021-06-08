"""
El Juego de Dados [versión 2.0]

A partir del juego de dados del Dos o Tres implementado en el Trabajo Práctico 1 se solicita ahora una nueva versión.
Las reglas se detallan a continuación:

Cantidad de jugadores: 2

Final del juego: Gana el jugador que alcance los x puntos o más,
siendo x un valor que se ingresa por teclado (validar que x sea mayor a 10).

Desarrollo del juego:

A pedido del público, sólo se implementa la segunda ronda de las reglas enunciadas en el TP1 anterior.
Es decir que, a su turno, cada jugador solo apuesta por par o impar.
Si acierta gana el puntaje equivalente al dado de mayor valor,
y adicionalmente este puntaje se duplica si todos los dados son de dicha apuesta.
Si pierde, resta el dado de menor valor (puede quedar con puntaje negativo).

Se debe mostrar por cada turno el valor de los dados y el puntaje parcial del jugador.

Al terminar el turno de ambos jugadores, se verifica si alguno de ellos alcanzó el puntaje objetivo.
Si no es así, vuelven a jugar ambos (cada uno debe completar su turno) hasta finalizar el juego.

Al terminar el juego, se debe mostrar el nombre y puntaje total obtenido de cada jugador
e informar el nombre del ganador. Si ambos jugadores llegaran a tener el mismo puntaje final,
gana aquel jugador que tenga la mayor cantidad de jugadas ganadas.
Si coinciden también en cantidad de jugadas, entonces es un empate.

Por último, se pide elaborar y mostrar las siguientes estadísticas:

    La cantidad de jugadas realizadas (recordando que una jugada consiste en los turnos de ambos jugadores).
    Si hubo al menos una jugada con puntaje empatado entre ambos jugadores.
    El puntaje promedio obtenido por jugada por cada jugador.
    El porcentaje de aciertos para cada jugador
    (considerando acierto si la suma de los dados coincidió con la apuesta apostada).
    Indicar también si el ganador es el que tuvo mayor porcentaje de aciertos.
    Si algún jugador ganó en al menos 3 turnos seguidos.

"""
import random

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Yo diagramé esto en mi cabeza así nomás       !!!!!
# pero si no se quieren hacer spoilers          !!!!!
# de como resolver el problema                  !!!!!
# entonces no sigan leyendo >:[                 !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Entradas:
puntaje_objetivo: int
nombre_jugador_1: str
nombre_jugador_2: str
apuesta_jugador_1: int  # o bool?
apuesta_jugador_2: int  # o bool?


# Proceso:

# ciclo del programa (opcion != 0)
# -- ingresar: nombre_jugador_1, nombre_jugador_2, puntaje_objetivo
# -- inicializar: contadores, acumuladores y banderas
# -- ciclo del juego (puntaje_total_1 < puntaje_objetivo and puntaje_total_2 < puntaje_objetivo)
# -- -- ingresar apuesta 1
# -- -- roll jugador 1
# -- -- proceso de calculo 1 (contadores y acumuladores)
# -- -- ingresar apuesta 2
# -- -- roll jugador 2
# -- -- proceso de calculo 2 (contadores y acumuladores)
# -- -- proceso de calculo jugada (contadores, acumuladores y banderas)
# -- -- informe puntaje parcial
# -- proceso de calculo final
# -- salida por pantalla de resultados


# posibles funciones utiles:
def solicitar_nombre():
    """Entradas: -- | Salidas: str"""
    pass

# verificar que no sean nombres iguales


def solicitar_puntaje_objetivo():
    """Entradas: -- | Salidas: int"""
    pass


def solicitar_apuesta():
    """Entradas: -- | Salidas: bool"""
    # par es True, impar es False
    pass


def tirar_dados():
    """Entradas: -- | Salidas: (int, int, int)"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    return (dado1, dado2, dado3)


def calcular_puntaje(dados, apuesta):
    """Entradas: (int, int, int), bool | Salidas: int"""
    puntaje = 0
    if check_acierto(dados, apuesta):
        puntaje += max(dados)
        if check_acierto_critico(dados, apuesta):
            puntaje *= 2
    else:
        puntaje -= min(dados)
    return puntaje


    pass


def print_resultados_parciales(nombre_jugador_1, nombre_jugador_2, puntaje_total_1, puntaje_total_2, jugadas_totales):
    """Entradas: str, str, int, int, int | Salidas: --"""
    pass


def check_acierto(dados, apuesta):
    """Entrada: (int, int, int), bool | Salida: bool"""
    pass

def check_acierto_critico(dados, apuesta):
    """Entrada: (int, int, int), bool | Salida: bool"""
    pass

# Salidas:



# Proceso:

# ciclo del programa (opcion != 0)
# -- ingresar: nombre_jugador_1, nombre_jugador_2, puntaje_objetivo
# -- inicializar: contadores, acumuladores y banderas
# -- ciclo del juego (puntaje_total_1 < puntaje_objetivo and puntaje_total_2 < puntaje_objetivo)
# -- -- ingresar apuesta 1
# -- -- roll jugador 1
# -- -- proceso de calculo 1 (contadores y acumuladores)
# -- -- ingresar apuesta 2
# -- -- roll jugador 2
# -- -- proceso de calculo 2 (contadores y acumuladores)
# -- -- proceso de calculo jugada (contadores, acumuladores y banderas)
# -- -- informe puntaje parcial
# -- proceso de calculo final
# -- salida por pantalla de resultados

opcion = None
while opcion.lower() != "x":
    print("Bienvenido! Presione \"enter\" para jugar. Ingrese X para salir")
    opcion = input()
    #Inicia el juego, solicita nombres y puntaje objetivo
    while nombre_jugador_1 == nombre_jugador_2:
        "A continuación, se les solicitara sus nombres"
        nombre_jugador_1 = solicitar_nombre()
        nombre_jugador_2 = solicitar_nombre()
        if nombre_jugador_1 == nombre_jugador_2:
            print("Advertencia: Si ud se llama igual que su rival, puede dirigirse al Registro Civil mas cercano para cambiarse el nombre, o directamente ingresar aquí un nombre diferente")
    solicitar_puntaje_objetivo()

    #Inicializar contadores, acumuladores y banderas
    jugadas_totales: int = 0
    jugadas_ganadas_1: int = 0
    jugadas_ganadas_2: int = 0

    puntaje_total_1: int = 0
    puntaje_total_2: int = 0

    aciertos_1: int = 0
    aciertos_2: int = 0

    jugadas_empatadas: bool = False
    tres_al_hilo: bool = False

    victorias_seguidas = 0
    ganador_jugada_actual = None
    ganador_jugada_anterior = None

    while (puntaje_total_1 < puntaje_objetivo and puntaje_total_2 < puntaje_objetivo):
        ganador_jugada_anterior = ganador_jugada_actual # ver si dejar acá o al fondo. Es lo mismo
        # Turno jugador 1
        apuesta_jugador_1 = solicitar_apuesta()
        dados_jugador_1 = tirar_dados()
        puntaje_total_1 += calcular_puntaje(dados_jugador_1)
        if check_acierto(dados_jugador_1, apuesta_jugador_1):
            aciertos_1 += 1

        # Turno jugador 2
        # Copiar de turno jugador 1

        # Proceso general
        # calcular ganador_jugada_actual
        # actualizar jugadas_ganadas_1 y jugadas_ganadas_2
        # actualizar jugadas_empatadas
        # actualizar tres_al_hilo ¿hacer función para esto?
        if ganador_jugada_actual == ganador_jugada_anterior:
            victorias_seguidas += 1
            if victorias_seguidas >= 3:
                tres_al_hilo = True
        else:
            victorias_seguidas = 0

        jugadas_totales += 1


        print_resultados_parciales(nombre_jugador_1,
                                   nombre_jugador_2,
                                   puntaje_total_1,
                                   puntaje_total_2,
                                   jugadas_totales)

    # Proceso general
    # Calcular ganador total -> encontrar_ganador(puntaje1_total_1, puntaje_total_2, jugadas_ganadas_1, jugadas_ganadas_2)
    # calcular porcentajes y promedios -> calcular_porcentaje(cantidad_1, cantidad_total)
    # revisar ganador mayor porcentaje de aciertos
    # Imprimir resultados y estadisticas: de todo!
    ganador: int
    ganador_mayores_aciertos: bool
    puntaje_promedio_1: float
    puntaje_promedio_2: float
    porcentaje_aciertos_1: float
    porcentaje_aciertos_2: float



print("Gracias por jugar! Nos vemos!")
