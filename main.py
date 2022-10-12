
# crear_tablero : None -> [[char]]
def crear_tablero():
    lista = [["" for i in range(0,8)] for i in range(0,8)]
    lista[3][3] = "B"
    lista[4][3] = "N"
    lista[4][4] = "B"
    lista[3][4] = "N"
    return lista

#crear_mapa_de_caracteres : None -> Map
def crear_mapa_de_caracteres():
    '''
        La función crea y retorna un diccionario con los caracteres valido que puede tomar el programa como indices, y cada uno tiene asociado
        la posición que representa en el tablero
    '''
    mapa = {}
    for x in range(0,9):
        mapa[chr(x+97)] = x
        mapa[chr(x+65)] = x
    return mapa

# sintaxis_correcta : String Dict -> Boolean
def sintaxis_correcta(jugada, caracteres_validos):
    try:

        return (caracteres_validos[jugada[0]] and int(jugada[1]) in range(0,8))
    except:

        return False

# jugada_valida 
def jugada_valida(jugada, tablero):
    direccion = (0,0)
    if tablero[jugada[0]][jugada[1]] == "":
        for i in range(8):
            direccion[]
    else:
            return False


#jugar : None -> None
def jugar():
    partida = open("partida.txt", "r")
    
    jugador1 = partida.readline().strip('\n')
    jugador2 = partida.readline().strip('\n')
    jugador_actual = partida.readline().strip('\n')

    carcteres_validos = crear_mapa_de_caracteres()
    tablero = crear_tablero()


    while  not(errores) and not(ganador):
        jugada = partida.readline().strip('\n')
        if sintaxis_correcta(jugada, caracteres_validos):
            coordenadas = (caracteres[jugada[0]],int(jugada[1]))
            if jugada_valida(jugada, tablero):
                pass
            else:
                    errores = False
        else:
            errores = False


