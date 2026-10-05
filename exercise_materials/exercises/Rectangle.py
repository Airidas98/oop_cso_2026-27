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




from Rectangle import Rectangle
import random


rectangles = []


for i in range(5):

    print("\nRectangle", i + 1)

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    number = random.randint(1, 10)

    print("Random number:", number)

    if number % 2 == 1:

        print("Number is odd - using default colour.")

        Rectangle = Rectangle(length, width)

    else:

        print("Number is even - enter a colour.")

        colour = input("Enter colour: ")

        Rectangle = Rectangle(length, width, colour)

    rectangles.append(Rectangle)


print("\n----------------------")
print("RECTANGLES")
print("----------------------")


for rectangle in rectangles:

    rectangle.display()

    print()

