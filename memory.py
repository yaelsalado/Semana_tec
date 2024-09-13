from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count= 0
tap_counter=0

def square(x, y):
    "Draw white square with black outline at (x, y)."
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
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global tap_count, tap_counter
    spot = index(x, y)
    mark = state['mark']

    tap_counter+=1

    if tap_counter==2:
        tap_count+=1
        tap_counter=0

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def reveal_all(): #Revelar fichas
    global hide
    hide = [False] * 64

def show_numbers():
    global show_all_numbers #revelar numeros
    show_all_numbers = True 

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y+10)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    up()
    goto(-180, 180)  #contador en la pantalla
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))

    if all(not tile for tile in hide):
        up()
        goto(0, 0)
        color('green')
        write('¡Ganaste!', align='center', font=('Arial', 30, 'bold'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
onkey(reveal_all, 's')
onkey(show_numbers,'n')
listen()
draw()
done()
