if __name__ == "__main__":
    students = [
        {"name": "Annie", "average_mark": 55},
        {"name": "Aine", "average_mark": 39},
        {"name": "Mira", "average_mark": 66},
        {"name": "Dan", "average_mark": 47}
    ]

    for i in range(len(students)):
        print(f"Student name: {students[i]["name"]}")
        print(f"Average score: {students[i]["average_mark"]}")

    for student_dict in students:
        if student_dict["name"] == "Dan":
            print(f"Dan's average mark: {student_dict["average_mark"]}")

    print(f"Dan's average mark: {students[3]["average_mark"]}")

    for student in students:
        if student["average_mark"] >= 50:
            print(student["name"])

    max_mark = -1
    name = None
    for i in range(len(students)):
        if students[i]["average_mark"] > max_mark:
            max_mark = students[i]["average_mark"]
            name = students[i]["name"]

    print(f"Student with highest mark ({max_mark}) was {name}")