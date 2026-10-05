#A1
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


from people import Person


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))


person = Person(first_name, last_name, age)


print("\nPerson Details")
print("First name:", person.first_name)
print("Last name:", person.last_name)
print("Age:", person.age)





