#B1
students = [
    {"name": "Evan", "marks": [65, 72, 81]},
    {"name": "Caleb", "marks": [45, 51, 48]},
    {"name": "Angelo", "marks": [82, 77, 91]},
    {"name": "Dorothy", "marks": [55, 63, 59]}
]

def calc_average(marks):
    total = sum(marks)
    average = total / len(marks)

    return average

print(calc_average([60, 70, 80]))

#B2
def calc_average(marks):
    return sum(marks) / len(marks)


for student in students:
    average = calc_average(student["marks"])
    print(student["name"], average)


for student in students:
    if student["name"] == "Caleb":
        average = calc_average(student["marks"])
        print("Caleb's average:", average)

#B3
def calc_average(marks):
    return sum(marks) / len(marks)


for student in students:
    average = calc_average(student["marks"])

    if average >= 50:
        print(student["name"])

#B4
def add_mark(student_dict, new_mark):
    student_dict["marks"].append(new_mark)

    add_mark(students[1], 66)

    print(students[1])