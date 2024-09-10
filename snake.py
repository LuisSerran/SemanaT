from random import randrange, choice
from turtle import *

from freegames import square, vector

snake_colors = ['blue', 'pink', 'yellow', 'purple', 'orange']
snake_color = choice(snake_colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(pos):
    """Return True if the position is inside boundaries."""
    return -200 < pos.x < 190 and -200 < pos.y < 190

def move():
    """Move snake forward one segment."""
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
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, 'green')
    update()

    ontimer(move, 100)

def move_food():
    """Move food randomly one step at a time."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = choice(directions)
    food_move = food + move_direction

    if inside(food_move):
        food.move(move_direction)

    ontimer(move_food, 500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
move_food()  
done()
