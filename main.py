
# crear_tablero : None -> [[char]]
def crear_tablero():
    lista = [["" for i in range(0,8)] for i in range(0,8)]
    lista[3][3] = "B"
    lista[4][3] = "N"
    lista[4][4] = "B"
    lista[3][4] = "N"
    return lista

#crear_mapa_de_caracteres : None -> Map
#
def crear_mapa_de_caracteres():
    '''
        La función crea y retorna un diccionario con los caracteres valido que puede tomar el programa como indices, y cada uno tiene asociado la posición que representa en el tablero.
    '''
    mapa = {}
    for x in range(0,9):
        mapa[chr(x+97)] = x
        mapa[chr(x+65)] = x
    return mapa

# sintaxis_correcta : String Dict -> Boolean
# Recibe la jugada y si no esta fuera del tablero devuelve True. En caso de que la jugada exceda
# los limites del tablero retorna False.
# ej: "B9" crear_mapa_de_caracteres -> False
def sintaxis_correcta(jugada, caracteres_validos):
    try:

        return (caracteres_validos[jugada[0]] and int(jugada[1:])-1 in range(0,8))
    except:

        return False


# buscar_ficha : (Int, Int) (Int, Int) [[Char]] Chart -> Boolean
# Dada una ficha y una dirección, busca si hay una ficha del 
def buscar_ficha(ficha, direccion, tablero, jugador_contrario):
    halloficha=False

    (x,y) = (ficha[0]+direccion[0],ficha[1]+direccion[1])
    (a,b) = direccion
    veces_desplazado = 1
    while not(halloficha) and x in range(8) and y in range(8):
        if tablero[x][y] == jugador_contrario:
            x +=1
            y +=1
            veces_desplazado +=1
        elif tablero[x][y] == "":
            veces_desplazado = -1 
            halloficha = True
        else:
            halloficha = True

    return veces_despazado if x in range(8) and y in range(8) else -1


# jugada_valida : (Int,Int) [[Char]] Char -> Boolean 
def jugada_valida(jugada, tablero, jugador_contrario):
    (a,b)= (-1,-1) # tupla para representar a la casilla adyacente que se esta quierendo ver
    (x,y) = jugada # coordenadas de la jugada
    if tablero[jugada[0]][jugada[1]] == "":
        for i in range(9):
            if tablero[x+a][y+b] == jugador_contrario:
                buscar_ficha((x+a, y+b), (a,b), tablero, jugador_contrario)
            a += 1
            if a == 2:
                b += 1
                a == -1
    else:
            return True


#jugar : None -> None
def jugar():
    partida = open("partida.txt", "r")
    
    jugador1 = partida.readline().strip('\n')
    jugador2 = partida.readline().strip('\n')
    jugador_actual = partida.readline().strip('\n')
    cambiar_jugador = {'B':'N','N':'B'}

    carcteres_validos = crear_mapa_de_caracteres()
    tablero = crear_tablero()
    errores = False


    while  not(errores) and not(ganador):
        jugada = partida.readline().strip('\n')
        if sintaxis_correcta(jugada, caracteres_validos):
            coordenadas = (caracteres[jugada[0]],int(jugada[1:])-1) # convertimos una string de caracteres validados en un par de coordenadas en el tablero
            errores = jugada_valida(jugada, tablero, jugador_actual)
            jugador_actual = cambiarjugador[jugador_actual]
        else:
            errores = True


