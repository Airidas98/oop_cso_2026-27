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