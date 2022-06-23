import random
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    @staticmethod
    def collision_with_food(food):
        food.refresh()
        return True

    def reset_high_score(self):
        for seg in self.segments:
            seg.goto(100, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def teletransport(self):
        x_random = random.randrange(-280, 280, 20)
        y_random = random.randrange(-280, 280, 20)
        self.head.goto(x_random, y_random)

    def get_food(self, target):
        # TODO 2: While Is heading towards food?
        # Todo 3: Change directions towards food on one axis (x axis, un less if the food is behind)
        # TODO 1: Locate Food and head position
        x_diff = target[0] - self.head.xcor()
        y_diff = target[1] - self.head.ycor()

        while x_diff > 0:
            self.right()
        while y_diff < 0:
            self.down()
        while y_diff > 0:
            self.up()
        while x_diff < 0:
            self.left()

        print(x_diff)
        print(y_diff)
