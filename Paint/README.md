# Actividad 2. Paint.

## Autores:

**Alejandro Guevara Olivares A00834438**
**Christian Gutierrez Briones A01284471**
**José Andrés Ordieres A01382904**

## Funciones Agregadas

**def circle1(start, end)**
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
