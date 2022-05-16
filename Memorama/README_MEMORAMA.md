# Integrantes
### Alejandro Guevara Olivares A00834438
### Christian Gutierrez Briones A01284471
### José Andrés Ordieres A01382904

# Links
### Link de Alejandro:
[Video Final Semana Tec](https://youtu.be/5L-JDn4FV0Q)

### Link de Christian:
[Video Final Semana Tec](https://youtu.be/dHbRuNk5X0U)

### Link de José:
[Video Final Semana Tec](https://youtu.be/ltE8xBrh01o)
# Código que Añadimos
### Desplegar los nombres de los integrantes
**Alejandro Guevara**
```

writer = Turtle()

def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(-200,220)
    writer.color('blue')
    writer.write('Alejandro Guevara Olivares A00834438', align = 'left', font=('Arial',10,'normal'))
    writer.goto(-200,210)
    writer.color('red')
    writer.write('Christian Gutierrez Briones A01284471', align = 'left', font=('Arial',10,'normal'))
    writer.goto(-200,200)
    writer.color('green')
    writer.write('José Andrés Ordieres A01382904', align = 'left', font=('Arial',10,'normal'))
info_alumnos()

setup(500, 500, 370, 0)

```
![7LZ5C-](https://i.makeagif.com/media/5-13-2022/7LZ5C-.gif)

### Detectar si todos los cuadros se han destapado
**Alejandro Guevara**
```

""" Esto va dentro de la función draw(), al final antes del update() """
if ganaste() == True:
        writer.hideturtle()
        writer.up()
        writer.goto(-130,-220)
        writer.color('blue')
        writer.write('GANASTE UN AUTO!!, FELICIDADES', align = 'left', font=('Arial',15,'normal'))
        
        
def ganaste():
    contador = 0
    for count in range(64):
        if hide[count] == False:
            contador = contador + 1
    if contador == 64:
        return True

```
![Z6Z-q9](https://i.makeagif.com/media/5-13-2022/Z6Z-q9.gif)
