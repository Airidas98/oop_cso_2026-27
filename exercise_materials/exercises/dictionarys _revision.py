#A1
if __name__ == "__main__":
    students = [
        {"name": "Annie", "average_mark": 55},
        {"name": "Aine", "average_mark": 39},
        {"name": "Mira", "average_mark": 66},
        {"name": "Dan", "average_mark": 47}
    ]

    for i in range(len(students)):
        print(f"Students name: {students[i]['name']}")
        print(f"Students average_mark: {students[i]['average_mark']}")
        print(f"students highest: {students[i]['average_mark']}")
#A2
    for student in students:
        if student["average_mark"] >= 50:
            print(student["name"])

#A3#
    highest = students[0]

    for student in students:
        if student["average_mark"] > highest["average_mark"]:
            highest = student

    print(highest["name"], "has the highest average:", highest["average_mark"])

