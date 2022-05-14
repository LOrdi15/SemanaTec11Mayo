"""
Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
 #PruebaChris3
from random import *
from turtle import *

from freegames import path

# La variable writer va a ser un objeto de tipo Turtle
writer = Turtle()

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
 
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    # Se despliega un mensage si ganaste() regresa True
    if ganaste() == True:
        writer.hideturtle()
        writer.up()
        writer.goto(-130,-220)
        writer.color('blue')
        writer.write('GANASTE UN AUTO!!, FELICIDADES', align = 'left', font=('Arial',15,'normal'))
        
    update()
    ontimer(draw, 100)
    

# Función ganaste, que regresa como valor de retorno True si la variable contador es igual a 64
def ganaste():
    contador = 0
    # Ciclo para pasar por todos los cuadros
    for count in range(64):
        # Se checa cada cuadro
        if hide[count] == False:
            contador = contador + 1
    if contador == 64:
        return True


# Función info_alumnos, que despliega los nombres de los integrantes
def info_alumnos():
    # Escondemos la flechita
    writer.hideturtle()
    # Escondemos la trayectoria de la flechita
    writer.up()
    # Info del primer integrante
    writer.goto(-200,220)
    writer.color('blue')
    writer.write('Alejandro Guevara Olivares A00834438', align = 'left', font=('Arial',10,'normal'))
    # Info del segundo integrante
    writer.goto(-200,210)
    writer.color('red')
    writer.write('Christian Gutierrez Briones A01284471', align = 'left', font=('Arial',10,'normal'))
    # Info del tercer integrante
    writer.goto(-200,200)
    writer.color('green')
    writer.write('José Andrés Ordieres A01382904', align = 'left', font=('Arial',10,'normal'))
# Llamado a la función
info_alumnos()


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()