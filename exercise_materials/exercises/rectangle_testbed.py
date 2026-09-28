from shapes import Rectangle


def create_rectangles():
    rectangles = []

    for i in range(5):

        print()
        print("Rectangle", i + 1)

        rectangle = Rectangle()

        rectangle.length = float(input("Enter length: "))
        rectangle.width = float(input("Enter width: "))
        rectangle.colour = input("Enter colour: ")

        rectangles.append(rectangle)

    return rectangles


def find_largest_rectangle(rectangles):

    largest = rectangles[0]

    for rectangle in rectangles:

        if rectangle.calc_area() > largest.calc_area():
            largest = rectangle

    return largest


def find_smallest_width(rectangles):

    smallest_position = 0

    for i in range(len(rectangles)):

        if rectangles[i].width < rectangles[smallest_position].width:
            smallest_position = i

    return smallest_position


def find_colour(rectangles, colour):

    matching_rectangles = []

    for rectangle in rectangles:

        if rectangle.colour.lower() == colour.lower():
            matching_rectangles.append(rectangle)

    return matching_rectangles


# Create the five rectangles
rectangles = create_rectangles()


# Find the rectangle with the largest area
largest = find_largest_rectangle(rectangles)

print()
print("Rectangle with the largest area:")
largest.display()
print("Area:", largest.calc_area())


# Find the rectangle with the smallest width
smallest_position = find_smallest_width(rectangles)

print()
print("Rectangle with the smallest width:")
print("Position in list:", smallest_position + 1)


# Find all red rectangles
red_rectangles = find_colour(rectangles, "red")

print()
print("Red rectangles:")

if len(red_rectangles) == 0:
    print("There are no red rectangles.")
else:

    for rectangle in red_rectangles:
        rectangle.display()


# Ask the user for another colour
search_colour = input("\nEnter a colour to search for: ")

matching_rectangles = find_colour(rectangles, search_colour)

print()
print("Rectangles with colour", search_colour + ":")

if len(matching_rectangles) == 0:
    print("There are no rectangles with this colour.")
else:

    for rectangle in matching_rectangles:
        rectangle.display()