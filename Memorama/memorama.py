
 #PruebaChris3
from random import *
from turtle import *

from freegames import path

# La variable writer va a ser un objeto de tipo Turtle
writer = Turtle()

car = path('car.gif')
#1
#Arreglo de emojis
tiles = ["\U0001F603","\U0001F601","\U0001F605","\U0001F923","\U0001F602","\U0001F642","\U0001F643","\U0001F609",
            "\U0001F970", "\U0001F929","\U0001F618","\U0001F911","\U0001F972","\U0001F917","\U0001F914","\U0001F928",
            "\U0001F611", "\U0001F612","\U0001F644","\U0001F614","\U0001F924","\U0001F634","\U0001F912","\U0001F915",
            "\U0001F922","\U0001F927","\U0001F975","\U0001F976","\U0001F974" ,"\U0001F920","\U0001F973","\U0001F978	"] * 2
state = {'mark': None}
hide = [True] * 64
N_taps = 0
win = 0

#Turtles para escribir en pantalla
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
#Turtle 5 escribe cuando se haya completado el memorama, por esto mismo la ocultamos con hideturtle()
t5 = turtle.Turtle()
t5.hideturtle()

#funcion que dibuja cuadrados blancos con perimetro negro
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#funcion que asigna la coordenada x y y con un cuadro 
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#funcion que convierte cuadros a coordenadas
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#funcion donde se actualiza el estado de los cuadros a base de los taps
def tap(x, y):
    # variable para contar el numero de taps
    global N_taps, win
    N_taps += 1
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        #cuando se encuentre un par igual usamos un contador para indicar cuando se completa el memorama
        win += 1
        #si se encuentran los 32 pares, se mostrara el mensaje que ganaste
        if(win == 32):
            t5.setposition(0, -230)
            t5.color('deep pink')
            style2 = ('Courier', 30, 'italic')
            t5.write("GANASTE!!" , font=style2, align='center')
            t5.hideturtle()
            
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
