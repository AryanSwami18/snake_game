from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_snake = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.all_snake.append(new_turtle)

    def extend(self):
        self.add_segment(self.all_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[seg_num - 1].xcor()
            new_y = self.all_snake[seg_num - 1].ycor()
            self.all_snake[seg_num].goto(new_x, new_y)
        self.all_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.all_snake[0].heading() != DOWN:
            self.all_snake[0].setheading(UP)

    def down(self):
        if self.all_snake[0].heading() != UP:
            self.all_snake[0].setheading(DOWN)

    def left(self):
        if self.all_snake[0].heading() != RIGHT:
            self.all_snake[0].setheading(LEFT)

    def right(self):
        if self.all_snake[0].heading() != LEFT:
            self.all_snake[0].setheading(RIGHT)
