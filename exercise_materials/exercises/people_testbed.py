from people import Person

# Create the first Person object
p1 = Person()

print("first person:")

if p1.left_handed:
    print(p1.first_name + " " + p1.second_name)
else:
    print((p1.first_name + " " + p1.second_name).upper())


# Create the second Person object
p2 = Person()

print()
print("Enter details for the second person:")

p2.first_name = input("Enter first name: ")
p2.second_name = input("Enter second name: ")
p2.age = int(input("Enter age: "))

left_handed = input("Are they left-handed? (yes/no): ")

if left_handed.lower() == "yes":
    p2.left_handed = True
else:
    p2.left_handed = False


# Display the second person's name
print()
print("second person:")

if p2.left_handed:
    print(p2.first_name + " " + p2.second_name)
else:
    print((p2.first_name + " " + p2.second_name).upper())