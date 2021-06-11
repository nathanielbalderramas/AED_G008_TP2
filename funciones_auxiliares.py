import random

def solicitar_nombre(quien=""):
    """Entradas: -- | Salidas: str"""
    if quien != "":
        quien += " "
    nombre = input(quien + "Ingrese su nombre: ")
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


def print_resultados_parciales(nombre_jugador_1, nombre_jugador_2, puntaje_total_1, puntaje_total_2, jugadas_totales):
    """Entradas: str, str, int, int, int | Salidas: --"""
    pass


def check_acierto(dados, apuesta):
    acierto = False
    d1, d2, d3 = dados
    paridad = (d1 + d2 + d3) % 2
    if apuesta is True and paridad == 0 or apuesta is False and paridad == 1:
        acierto = True
    return acierto


def check_acierto_critico(dados, apuesta):
    """Entrada: (int, int, int), bool | Salida: bool"""
    pass


def jugada(nombre):
    """Entrada: str | Salida: (int, bool)"""
    print("Turno de {}\nExitos!\n".format(nombre))
    apuesta = solicitar_apuesta()
    dados = tirar_dados()
    print("Tus dados son: {}, {}, {}".format(*dados))
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
        puntaje += "¡Maravillosa jugada! O_O"
    print(msj)
    return puntaje, acierto


def calcular_promedio(acumulador, contador):
    """Entradas: int, int | Salidas: float"""
    pass


def calcular_porcentaje(x, total):
    """Entradas: int, int | Salidas: float"""
    # Recomendaría que el float sea redondeado a 1
    pass


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

