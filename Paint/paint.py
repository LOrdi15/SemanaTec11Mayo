"""Paint, for drawing shapes.

Jose Andres Ordieres
Alejandro Guevara
Christian Gutierrez Briones

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

# La variable writer va a ser un objeto de tipo Turtle
writer = Turtle()

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función circle1 (cambiamos el nombre para diferenciar de la función "circle" ya existente en la librería Turtle)
def circle1(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    # Calculamos el radio
    radio = (end.x - start.x)/2
    
    begin_fill()
    # Hacemos uso de la función ya existente "circle(radio, extent, steps)"
    circle(radio, None, None)
    
    end_fill()
 
   

def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.y)
        left(90)
        forward(end.x - start.y)
        left(50)
    end_fill()
    
     

def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value
    
# Función nombres, que despliega los nombres de los integrantes
def nombres():
    # Escondemos la flechita
    writer.hideturtle()
    writer.up()
    # Info del primer integrante
    writer.goto(-200,190)
    writer.color('light sea green')
    writer.write('Alejandro Guevara Olivares A00834438', align = 'left', font=('Arial',10,'normal'))
    # Info del segundo integrante
    writer.goto(-200,175)
    writer.color('chartreuse')
    writer.write('Christian Gutierrez Briones A01284471', align = 'left', font=('Arial',10,'normal'))
    # Info del tercer integrante
    writer.goto(-200,160)
    writer.color('maroon')
    writer.write('José Andrés Ordieres A01382904', align = 'left', font=('Arial',10,'normal'))
# Llamado a la función
nombres()

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
# Añadimos color amarillo
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle1), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
