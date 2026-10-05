class Rectangle:

    def __init__(self, length, width, colour="Blue"):
        self.length = length
        self.width = width
        self.colour = colour

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Colour:", self.colour)

        rectangle1 = Rectangle(10, 5)

        rectangle1.display()

