### Alejandro Guevara Olivares A00834438
### Christian Gutierrez Briones A01284471
### José Andrés Ordieres A01382904

### Link de Alejandro:

### Link de Christian:

### Link de José:

## Desplegar los nombres de los integrantes
**Alejandro Guevara**
´´´

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

´´´

## Detectar si todos los cuadros se han destapado
**Alejandro Guevara**
´´´

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

´´´
