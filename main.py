# crear_tablero : None -> [[char]]
def crear_tablero():
    lista = [[" " for i in range(8)] for i in range(8)]
    lista[3][3] = "B"
    lista[4][3] = "N"
    lista[4][4] = "B"
    lista[3][4] = "N"
    return lista

# crear_contorno : None -> Set((Int,Int))
def crear_contorno():
    contorno = set()
    #lista = [C3, D3, E3, F3, C4, F4, C5, F5, C6, D6, E6, F6]
    lista = [(2,2),(3,2),(4,2),(5,2),(2,3),(5,3),(2,4),(5,4),(2,5),(3,5),(4,5),(5,5)]
    for i in lista:
        contorno.add(i)

    return contorno
# sintaxis_correcta : String -> Boolean
# Recibe la jugada y si no esta fuera del tablero devuelve True. En caso de que la jugada exceda
# los limites del tablero, o su sintaxis sea incorrecta, retorna False.
# ej: "B9" -> False
def sintaxis_correcta(jugada):
    try:
        return ((ord(jugada[0]) in range(97,105) or ord(jugada[0]) in range(65,73)) and int(jugada[1:])-1 in range(0,8))
    except: 
        return False


# buscar_ficha : (Int, Int) (Int, Int) [[Char]] Chart -> Boolean
# Dada una ficha y una dirección, busca si hay una ficha del jugador contrario en dicha direccion
def buscar_ficha(ficha, direccion, tablero, jugador_contrario):
    
    halloficha=False
    (a,b) = direccion
    (x,y) = (ficha[0] + a,ficha[1] + b)
    veces_desplazado = 1
    
    while not(halloficha) and x in range(8) and y in range(8):
        if tablero[x][y] == jugador_contrario:
            x += a
            y += b
            veces_desplazado +=1
        elif tablero[x][y] == " ":
            veces_desplazado = 0 
            halloficha = True
        else:
            halloficha = True

    return veces_desplazado if x in range(8) and y in range(8) else 0


# jugada_valida : (Int,Int) [[Char]] Char Boolean -> Boolean
# Dada una posicion valida, un tablero, el color del jugador actual, y un modo,
# determina si esa posicion puede reducir la cantidad de fichas del equipo contrario y altera el tablero si el modo es True.
# Si la jugada es invalida retorna False y si la jugada es valida retorna True.
def jugada_valida(jugada, tablero, jugador_actual, modo):
    (y, x) = jugada 
    pos_valida = False
    vectores = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)) #todas las posibles direcciones adyacentes
    cambiar_ficha = {'B':'N','N':'B'}
    jugador_contrario = cambiar_ficha[jugador_actual]

    if tablero[x][y] == " ":
        for (a,b) in vectores:
            if  x+a in range(8) and y+b in range(8) and tablero[x+a][y+b] == cambiar_ficha[jugador_actual] : # esto es rapido, lo juro
                veces_desplazado = buscar_ficha((x+a, y+b), (a,b), tablero, jugador_contrario)
                if(veces_desplazado):
                    pos_valida = True
                    if(modo): voltear((x,y),(a,b),veces_desplazado, tablero)
    
    if(pos_valida and modo):
        tablero[x][y] = cambiar_ficha[jugador_contrario]

    return pos_valida

#voltear : (Int,Int) (Int,Int) Int [[Char]] -> None
#Dada una posicion, una direccion, un numero n y un tablero,
#Cambia el color de n fichas apartir de la posicion desplazandose por la direccion
def voltear(posicion, direccion, veces_desplazado, tablero):
    (x,y) = posicion
    (a,b) = direccion
    cambiar_ficha = {'B':'N','N':'B'}
    for i in range(veces_desplazado):
        x += a
        y += b
        tablero[x][y] = cambiar_ficha[tablero[x][y]]

#agregar_a_contorno : (Int, Int, Char) Set((Int,Int)) [[Char]]
def agregar_a_contorno(coordenadas, contorno, tablero):
    (x,y) = coordenadas
    vectores = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))

    for (a,b) in vectores:
        if x+a in range(8) and y+b in range(8) and tablero[x+a][y+b] == " ":
            contorno.add((x+a , y+b))


#jugar : None -> None
def jugar():
    partida = open("partida.txt", "r")
    
    (jugador1, color_j1) = partida.readline().strip('\n').split(",")
    (jugador2, color_j2) = partida.readline().strip('\n').split(",")
    jugador_actual = partida.readline().strip('\n')
    cambiar_jugador = {'B':'N','N':'B'}
    nombres = {color_j1:jugador1,color_j2:jugador2}

    tablero = crear_tablero()
    contorno = crear_contorno()
    errores = False
    ganador = False

    while  not(errores) and not(ganador):
        jugada = partida.readline().strip('\n')
        if sintaxis_correcta(jugada):
            coordenadas = (ord(jugada[0].upper())-65,int(jugada[1:])-1) #convierte la jugada en una coordenada del tablero
            errores = not(jugada_valida(coordenadas, tablero, jugador_actual, True))
            if not(errores):
                contorno.remove(coordenadas) # si la ficha era una jugada valida, entonces pertenece al contorno
                agregar_a_contorno(coordenadas, contorno, tablero)
        elif jugada == "":
            errores = False
            for (x,y) in contorno:
                coordenadas = (x,y)
                if(not(jugada_valida(coordenadas, tablero, jugador_actual, False))):
                    errores = True
        else:
            errores = True
        jugador_actual = cambiar_jugador[jugador_actual]
    for i in tablero:
        print(i)
    if errores:
        jugador_actual = cambiar_jugador[jugador_actual]
        output = ("No se podia saltear la jugada" if jugada == "" else "Las coordenadas fueron incorrectas")
        print(output)
        print("Ultimas coordenadas tomadas:", coordenadas)
        print("Que decia en el archivo:","\"", jugada, "\"")
    print("Le tocaba a", jugador_actual)
    partida.close()


