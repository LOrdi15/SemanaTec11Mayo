# Actividad 2. Paint.

## Autores:

**Alejandro Guevara Olivares A00834438**

**Christian Gutierrez Briones A01284471**

**José Andrés Ordieres A01382904**

## Funciones Agregadas

### Un color nuevo
- Añade un color nuevo a la lista de opciones (amarillo) 
- Autor: Alejandro Guevara Olivares
- Código:
```
# Añadimos color amarillo
onkey(lambda: color('yellow'), 'Y')
```
![gfa3eB](https://i.makeagif.com/media/5-13-2022/gfa3eB.gif)

### def circle1(start, end)
- Dibuja un círculo 
- Autor: Alejandro Guevara Olivares
- Código:
```
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
```
![oUJJTW](https://i.makeagif.com/media/5-13-2022/oUJJTW.gif)

### def nombres()
- Desplega los nombres y las matrículas de los integrantes del equipo
- Autor: Alejandro Guevara Olivares
- Código:
```
# La variable writer va a ser un objeto de tipo Turtle
writer = Turtle()

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
```
![k0b7AG](https://i.makeagif.com/media/5-13-2022/k0b7AG.gif)
