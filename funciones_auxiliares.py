import random


def solicitar_nombre(quien=""):
    """Entradas: -- | Salidas: str"""
    if quien != "":
        quien += " "
    nombre = ""
    while nombre == "":
        nombre = input(quien + "Ingrese su nombre por favor: ")
    return nombre


def cargar_entero_con_tope_minimo(tope_minimo, mensaje=None):
    if mensaje:
        print(mensaje)
    x = int(input("Ingrese un número mayor a " + str(tope_minimo) + ": "))
    while x <= tope_minimo:
        print("El valor ingresado no es válido")
        x = int(input("Ingrese un número mayor a " + str(tope_minimo) + ": "))
    return x


def solicitar_puntaje_objetivo():
    x = 0
    while x <= 10:
        x = int(input("Ingrese la cantidad de puntos que se deben alcanzar para que finalice la partida: "))
        if x <= 10:
            print("Ingrese un valor mayor a 10")
    return x


def solicitar_apuesta(mensaje_previo=None):
    """Entradas: str | Salidas: bool"""
    # par es True, impar es False
    apuesta = None
    if mensaje_previo:
        print(mensaje_previo)
    while apuesta != "s" and apuesta != "n":
        print("Debe apostar por resultado par o impar.")
        apuesta = input("¿Desea apostar por par? (s/n)\n")
        apuesta = apuesta.lower()

    if apuesta == "s":
        return True
    else:
        return False


def tirar_dados():
    """Entradas: -- | Salidas: (int, int, int)"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    return dado1, dado2, dado3


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


def print_resultados_parciales(nombre_jugador_1, nombre_jugador_2, puntaje_jugada_1, puntaje_jugada_2,
                               puntaje_total_1, puntaje_total_2, jugadas_totales):
    """Entradas: str, str, int, int, int | Salidas: --"""
    msj = "-"*60 + "\n"
    msj += "Puntajes de la jugada N° {}:\n".format(jugadas_totales)
    msj += "Nombre".center(20) + "| Parcial | Acumulado \n"
    msj += "{}".format(nombre_jugador_1).center(20)
    msj += "|" + "{:3d}".format(puntaje_jugada_1).center(9) + "|" + "{:3d}".format(puntaje_total_1).center(11) + "\n"
    msj += "{}".format(nombre_jugador_2).center(20)
    msj += "|" + "{:3d}".format(puntaje_jugada_2).center(9) + "|" + "{:3d}".format(puntaje_total_2).center(11)
    print(msj)


def es_par(num):
    # devuelve True si es par
    if num % 2 == 0:
        return True
    else:
        return False


def check_acierto(dados, apuesta):
    acierto = False
    d1, d2, d3 = dados
    paridad = (d1 + d2 + d3) % 2
    if apuesta is True and paridad == 0 or apuesta is False and paridad == 1:
        acierto = True
    return acierto


def check_acierto_critico(dados, apuesta):
    """Entrada: (int, int, int), bool | Salida: bool"""
    d1, d2, d3 = dados
    if es_par(d1) == apuesta and es_par(d2) == apuesta and es_par(d3) == apuesta:
        acierto_critico = True
    else:
        acierto_critico = False
    return acierto_critico


def jugada(nombre):
    """Entrada: str | Salida: (int, bool)"""
    print("Turno de {}\nExitos!".format(nombre))
    apuesta = solicitar_apuesta()
    input("Presione enter para lanzar los dados...")
    print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
    dados = tirar_dados()
    print("Tus dados son: [{}] [{}] [{}]".format(*dados))
    input()  # Pausa para el jugador
    acierto = check_acierto(dados, apuesta)
    puntaje = calcular_puntaje(dados, apuesta)
    msj = "Tu puntaje para esta jugada es de: {}\n".format(puntaje)

    # Brillantina Emocional
    if puntaje < -8:
        msj += "¿Has considerado dedicarte a otra cosa? :/"
    elif puntaje < 0:
        msj += "Que mal :c"
    elif puntaje < 8:
        msj += "Nada mal :)"
    else:
        msj += "¡Maravillosa jugada! O_O"
    print(msj+"\n")
    return puntaje, acierto


# puntaje_promedio_1 = calcular_promedio(puntaje_total_1, jugadas_totales)
def calcular_promedio(acumulador, contador):
    """Entradas: int, int | Salidas: float"""
    promedio = acumulador / contador
    return round(promedio, 2)


# porcentaje_aciertos_1 = calcular_porcentaje(aciertos_1, jugadas_totales)
def calcular_porcentaje(num, total):
    """Entradas: int, int | Salidas: float"""
    # Recomendaría que el float sea redondeado a 1
    porcentaje = (num / total) * 100
    return round(porcentaje, 2)


def encontrar_ganador(puntaje_1, puntaje_2, victorias_1, victorias_2):
    # Determinación del ganador
    if puntaje_1 > puntaje_2:
        ganador = 1
    elif puntaje_1 < puntaje_2:
        ganador = 2
    else:
        if victorias_1 > victorias_2:
            ganador = 1
        elif victorias_1 < victorias_2:
            ganador = 2
        else:
            ganador = 0

    # revisar si el ganador  tiene mayor porcentaje de aciertos
    ganador_mayores_aciertos = False
    if ganador == 1:
        if victorias_1 > victorias_2:
            ganador_mayores_aciertos = True
    elif ganador == 2:
        if victorias_1 < victorias_2:
            ganador_mayores_aciertos = True

    return ganador, ganador_mayores_aciertos


def print_resultados_finales(ganador, ganador_mayor_aciertos, nombre_jugador_1, nombre_jugador_2,
                             jugadas_totales, jugadas_empatadas, tres_al_hilo,
                             puntaje_promedio_1, puntaje_promedio_2, porcentaje_aciertos_1, porcentaje_aciertos_2):
    # Traducir banderas a string
    if jugadas_empatadas:
        jugadas_empatadas = "SI"
    else:
        jugadas_empatadas = "NO"

    if tres_al_hilo:
        tres_al_hilo = "SI"
    else:
        tres_al_hilo = "NO"

    # Imprimir resultados y estadisticas: de todo!
    print("\n" + "=" * 60)
    print("FIN DE LA PARTIDA".center(60))
    print("=" * 60 + "\n")

    if ganador == 0:
        print("El juego ha concluído en un empate ¯\\_(ツ)_/¯ \n¡Eso no pasa todos los días!")
    elif ganador == 1:
        print("El juego ha concluído con una victoria para {}!".format(nombre_jugador_1))
    elif ganador == 2:
        print("El juego ha concluído con una victoria para {}!".format(nombre_jugador_2))
    else:
        print("WTF just happened?")  # DEBUG

    if ganador != 0:
        print("¡¡FELICIDADES!!")
    if ganador_mayor_aciertos:
        print("El ganador del juego fue también quien obtuvo la mayor cantidad de aciertos en sus apuestas!")

    print("\n" + "-" * 60)
    print("Estadísticas de la partida".center(60))
    print("-" * 60)
    print("Jugadas totales: {}".format(jugadas_totales))
    print("Puntaje Promedio de {}: {}".format(nombre_jugador_1, puntaje_promedio_1))
    print("Puntaje Promedio de {}: {}".format(nombre_jugador_2, puntaje_promedio_2))
    print("Porcentaje de Aciertos de {}: {}%".format(nombre_jugador_1, porcentaje_aciertos_1))
    print("Porcentaje de Aciertos de {}: {}%".format(nombre_jugador_2, porcentaje_aciertos_2))
    print("Jugadas empatadas: {}".format(jugadas_empatadas))
    print("Tres Al Hilo: {}".format(tres_al_hilo))
    print("-" * 60 + "\n")
