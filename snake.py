from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
food_aim = vector(10, 0)  # Dirección inicial de la comida

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Move food randomly one step inside the boundaries."
    # Mueve la comida en su dirección actual
    food.move(food_aim)

    # Cambia la dirección si la comida llega a los límites
    if not inside(food):
        food_aim.x = randrange(-1, 2) * 10  # Cambia aleatoriamente la dirección en x
        food_aim.y = randrange(-1, 2) * 10  # Cambia aleatoriamente la dirección en y

    # Asegúrate de que la comida se quede dentro de los límites
    if not inside(food):
        food.x = max(min(food.x, 190), -190)
        food.y = max(min(food.y, 190), -190)

    ontimer(move_food, 500)  # La comida se moverá cada 500 milisegundos

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()  # Inicia el movimiento de la comida
done()
