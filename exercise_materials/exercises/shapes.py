class Rectangle:

    def __init__(self):
        self.length = 10
        self.width = 5
        self.colour = "blue"

    def display(self):
        print(
            f"Rectangle[length={self.length}, "
            f"width={self.width}, "
            f"colour={self.colour}]"
        )

    def calc_area(self):
        area = self.length * self.width
        return area


# Create a rectangle
rectangle = Rectangle()

# Display the rectangle
rectangle.display()

# Calculate and display the area
print("Area:", rectangle.calc_area())