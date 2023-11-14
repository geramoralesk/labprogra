import random

class Tablero:
    def __init__(self):
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)]

    def mostrar_tablero(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        letras = 'ABCDEFGHIJ'
        for i in range(10):
            fila = ' '.join(self.tablero[i])
            print(f"{letras[i]} {fila}")

class Barco:
    def __init__(self, size):
        self.size = size
        self.hits = 0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()
        self.barcos = {
            'pequenos': [Barco(3) for _ in range(3)],
            'grandes': [Barco(5) for _ in range(2)]
        }

def colocar_barcos(jugador):
    for size in [3, 3, 3, 5, 5]:
        print(f"{jugador.nombre}, coloca un barco de tamaño {size}.")
        fila, columna, orientacion = input("Ingresa fila (A-J), columna (1-10), y orientación (H/V): ").upper(), int(input()), input().upper()
        colocar_barco(jugador, size, fila, columna, orientacion)

def colocar_barco(jugador, size, fila, columna, orientacion):
    letras = 'ABCDEFGHIJ'
    fila_index = letras.index(fila)
    columna -= 1

    if orientacion == 'H':
        for i in range(size):
            jugador.tablero.tablero[fila_index][columna + i] = 'O'
    elif orientacion == 'V':
        for i in range(size):
            jugador.tablero.tablero[fila_index + i][columna] = 'O'
    else:
        print("Orientación no válida. Inténtalo de nuevo.")
        colocar_barco(jugador, size, input(), int(input()), input().upper())

def turno(jugador, oponente):
    print(f"{jugador.nombre}, es tu turno.")
    fila, columna = input("Ingresa fila (A-J) y columna (1-10) para disparar: ").upper(), int(input())
    letras = 'ABCDEFGHIJ'
    fila_index = letras.index(fila)

    if oponente.tablero.tablero[fila_index][columna - 1] == 'O':
        print("¡Acertaste en un barco!")
        for barco in oponente.barcos['pequenos'] + oponente.barcos['grandes']:
            for i in range(barco.size):
                if barco.size == 3 and oponente.tablero.tablero[fila_index][columna - 1 + i] == 'O':
                    barco.hits += 1
                elif barco.size == 5 and oponente.tablero.tablero[fila_index + i][columna - 1] == 'O':
                    barco.hits += 1

        oponente.tablero.tablero[fila_index][columna - 1] = 'X'
        if check_ganador(oponente):
            print(f"{jugador.nombre} ha ganado. ¡Felicidades!")
            return True
    else:
        print("Agua. No has acertado en un barco.")
        oponente.tablero.tablero[fila_index][columna - 1] = '-'

    return False

def check_ganador(jugador):
    for barco in jugador.barcos['pequenos'] + jugador.barcos['grandes']:
        if barco.hits < barco.size:
            return False
    return True

def main():
    jugadores = [
        Jugador("Jugador 1"),
        Jugador("Jugador 2")
    ]

    for jugador in jugadores:
        colocar_barcos(jugador)

    input("Presiona Enter para comenzar el juego.")

    turnos = random.sample(jugadores, len(jugadores))  

    while True:
        for i in range(len(jugadores)):
            jugador_actual = turnos[i]
            oponente = jugadores[1 - i]  
            if turno(jugador_actual, oponente):
                return

if __name__ == "__main__":
    main()
