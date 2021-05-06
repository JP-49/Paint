from turtle import *
from freegames import vector
import turtle


def line(start, end):
    "Draw line from start to end."
    up()	#Levanta la pluma
    goto(start.x, start.y)
    down()	#Baja la pluma, comienza a dibujar
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()	#Comienza a llenar la forma del dibujo

    for count in range(4):	#Traza el cuadrado calculando su longitud y girando 90 grados 4 veces
        forward(end.x - start.x)
        left(90)

    end_fill()	#Finaliza el relleno de la forma


def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO


def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()


    for count in range(2):	#El procedimiento se repite 2 veces
        forward(end.x - start.x)	#Para calcular la base del rectangulo, tomará los clicks en el eje x
        left(90)	#Gira 90 grados para continuar con la altura
        forward(end.y - start.y)	#Para calcular la altura con los clicks seleccionados en el eje y
        left(90)

    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):	#Traza el triangulo calculando su longitud y girando 120 grados 3 veces
        forward(end.x - start.x)
        left(120)
        
    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value

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
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
