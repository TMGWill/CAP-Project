import random
import turtle


class CAP_A:
    """
    This creates the CAP_A class which uses the values given
    from the CAP_P class methods.
    """

    def __init__(self, start="carefree", loop=10, side_A=3, side_B=10, length=100, color="random"):
        """
        :param start: determines starting position for the art_brush
        :param loop: determines how many times the create_art method will loop
        :param side_A: determines the minimum range of sides for the shape
        :param side_B: determines the maximum range of sides for the shape
        :param length: determines the size of the shape(s)
        :param color: determines the color of the shape(s)
        """

        self.art_start = start
        self.art_start_x = 0
        self.art_start_y = 0
        self.art_loop = loop
        self.art_sides_A = side_A
        self.art_sides_B = side_B
        self.art_length = length
        self.art_color = color
        self.art_brush = turtle.Turtle()

    def create_art(self):
        """
        This draws to the screen either with the initial
        parameters it's been given or ones that are
        set by the user.

        :return: None
        """

        wn = turtle.Screen()
        wn.colormode(255)

        self.art_brush.speed(10)

        for i in range(self.art_loop):
            if self.art_start == "carefree":
                self.art_start_x = random.randrange(-600, 600)
                self.art_start_y = random.randrange(-300, 300)

            elif self.art_start =="left high":
                self.art_start_x = random.randrange(-600, -200)
                self.art_start_y = random.randrange(100, 300)
            elif self.art_start =="left middle":
                self.art_start_x = random.randrange(-600, -200)
                self.art_start_y = random.randrange(-100, 100)
            elif self.art_start =="left bottom":
                self.art_start_x = random.randrange(-600, -200)
                self.art_start_y = random.randrange(-300, -100)

            elif self.art_start =="middle high":
                self.art_start_x = random.randrange(-200, 200)
                self.art_start_y = random.randrange(100, 300)
            elif self.art_start =="middle middle":
                self.art_start_x = random.randrange(-200, 200)
                self.art_start_y = random.randrange(-100, 100)
            elif self.art_start =="middle bottom":
                self.art_start_x = random.randrange(-200, 200)
                self.art_start_y = random.randrange(-300, -100)

            elif self.art_start =="right high":
                self.art_start_x = random.randrange(200, 600)
                self.art_start_y = random.randrange(100, 300)
            elif self.art_start =="right middle":
                self.art_start_x = random.randrange(200, 600)
                self.art_start_y = random.randrange(-100, 100)
            elif self.art_start =="right bottom":
                self.art_start_x = random.randrange(200, 600)
                self.art_start_y = random.randrange(-300, -100)

            sides = random.randrange(self.art_sides_A, self.art_sides_B)

            if self.art_color == "random":
                color_a = random.randint(0, 255)
                color_b = random.randint(0, 255)
                color_c = random.randint(0, 255)
                self.art_brush.color(color_a, color_b, color_c)
            else:
                self.art_brush.color(self.art_color)

            self.art_brush.setpos(self.art_start_x, self.art_start_y)

            for ii in range(sides):
                self.art_brush.forward(self.art_length)
                self.art_brush.right(360/sides)

        wn.exitonclick()



