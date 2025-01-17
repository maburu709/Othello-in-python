
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

#agregar_a_contorno : (Int, Int, Char) Set((Int,Int)) [[Char]] -> None
# Toma una jugada, un contorno y un tablero y agrega al contorno todas los espacios adyacentes a la jugada, tal que
# el espacio adyacente no esta ocupado
def agregar_a_contorno(coordenadas, contorno, tablero):
    (x,y) = coordenadas
    vectores = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))

    for (a,b) in vectores:
        if x+a in range(8) and y+b in range(8) and tablero[x+a][y+b] == " ":
            contorno.add((x+a , y+b))

#hay_ganador: [[Char]] -> Char
#Analiza si no hay más posibles jugadas válidas para ninguno de los equipos.
#En caso de que ninguno de los dos equipos tenga mas movimientos, retorna el equipo con mas fichas
#de su color en el tablero.
#En caso de que no haya un ganador retorna "".
def hay_ganador(tablero, contorno):
    fichasB=0
    fichasN=0
    existeganador=True
    for k in contorno:
        if jugada_valida(k, tablero, "B" , False) or jugada_valida(k, tablero, "N", False):
            existeganador=False
    if (existeganador==False):
        return ""
    for i in range(8):
        for j in range (8):
            if (tablero[i][j]=="N"):
                fichasN=fichasN+1
            elif (tablero[i][j]=="B"):
                fichasB=fichasB+1
    if (fichasB>fichasN):
        return "B"
    else:
        return "N"

#imprimir: [[Char]] -> None
#Dado un tablero, imprime el contenido en un formato amigable para su lectura
def imprimir(tablero):
    columnas = ["A","B","C","D","E","F","G","H"]
    i = 0 # perdonenme la falta de respeto pero esta variable no se me ocurre como llamarla
    cantidad_columnas = len(columnas)
    while i < cantidad_columnas:
        print(f"\t| {columnas[i]}", end = "") 
        i +=1
    print()
    for fila in range(1,9):
        print(f"{fila} ", end = "" )
        for casillero in tablero[fila-1]:
            print(f"\t|",casillero, end = "")
        print()
    
#intentar_saltear: [[Char]] Char Set((Int,Int)) -> Boolean
#la función toma un tablero, el jugador actual y el contorno de las fichas jugadas
#si el jugador actual no puede jugar y el otro jugador si puede, entonces se saltó el turno correctamente, retorna True
#si el jugador actual puede jugar entonces no se puede saltear, retorna False
#si el jugador actual no puede jugar y el otro jugador tampoco entonces debió haber terminado el juego, retorna False
def intentar_saltear(tablero, jugador_actual, contorno):
    
    cambiar_jugador = {'B':'N','N':'B'}
    puede_jugar_actual = False
    puede_jugar_contrario = False

    for coordenadas in contorno:
        if(jugada_valida(coordenadas, tablero, jugador_actual, False)):
            puede_jugar_actual = True
        if(jugada_valida(coordenadas, tablero, cambiar_jugador[jugador_actual], False)):
            puede_jugar_contrario = True
    
    return not(puede_jugar_actual) and puede_jugar_contrario

#que_tipo_de_error String String -> String
#Retorna un mensaje persoalizado de error, dependiendo de la jugada final que se intentó hacer.
def que_tipo_de_error(jugada_final, nombre_j_final):
    error_handler = {
        
        "": "No se ingresó ninguna jugada",
        
        " " : "No se podía saltear el turno"
        
    }
    error_de_posicion = f"El jugador {nombre_j_final}, trato de colocar una ficha en {jugada_final} y esa es una posicion invalida"
    return(error_handler.get(jugada_final, error_de_posicion))

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
    hubo_error = False
    hubo_ganador = False
    jugada = partida.readline()
    jugada_final = jugada

    while  not(hubo_error) and not(hubo_ganador) and jugada != "":
        jugada = jugada.strip("\n")
        if jugada == "":
            hubo_error = (not intentar_saltear(tablero,jugador_actual,contorno))
            jugada_final = " "
        elif sintaxis_correcta(jugada):
            coordenadas = (ord(jugada[0].upper())-65,int(jugada[1:])-1) #convierte la jugada en una coordenada del tablero
            hubo_error = not(jugada_valida(coordenadas, tablero, jugador_actual, True))
            jugada_final = jugada
            if not(hubo_error):
                contorno.remove(coordenadas) # si la ficha era una jugada valida, entonces pertenece al contorno
                agregar_a_contorno(coordenadas, contorno, tablero)
        else:
            hubo_error = True
            jugada_final = jugada
        jugador_actual = cambiar_jugador[jugador_actual]
        jugada = partida.readline()
    imprimir(tablero)
    if hubo_error:
        jugador_actual = cambiar_jugador[jugador_actual]
        output = que_tipo_de_error(jugada_final, nombres[jugador_actual])
        print(output)
        print("Ultimas coordenadas tomadas:", coordenadas)
    print("Le tocaba a", jugador_actual)
    partida.close()

#generador_tableros_prueba: (Chart) -> [[Chart]]
#Genera tableros de prueba a usarse en los pytest con una tupla de casillas que van a estar
def generador_tableros_prueba(casillas):
    tablero=crear_tablero
    

#Test de la función sintaxis_correcta()
def test_sintaxis_correcta():
    sintaxis_correcta("F90") == False
    sintaxis_correcta("G6") == True
    sintaxis_correcta("7F") == False
    sintaxis_correcta("f5") == False

#Test de la función buscar_ficha()
def test_buscar_ficha():
    
    pass
    