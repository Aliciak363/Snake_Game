from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.new_squares = []
        self.draw_snake()
        self.head = self.new_squares[0]

    def draw_snake(self):
        for position in STARTING_POSITIONS:
             self.add_square(position)

    def add_square(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.new_squares.append(square)

    def extend_tail_snake(self):       #extend = predlzit
        #add a new square to the snake
        self.add_square(self.new_squares[-1].position())    #-1 je posledna pozicia v liste

    def move_snake(self):
        for square_num in range(len(self.new_squares) - 1, 0, -1):  #-1 je posledna pozicia v len(new_squares), 0 je prve cislo,
                                                                    # a -1 je ze sa odpocitavaju miesta po -1
            line_x = self.new_squares[square_num - 1].xcor()
            line_y = self.new_squares[square_num - 1].ycor()
            self.new_squares[square_num].goto(line_x, line_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for square in self.new_squares:
            square.goto(1000, 1000)
        self.new_squares.clear()
        self.draw_snake()
        self.head = self.new_squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)