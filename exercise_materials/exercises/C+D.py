basket = [
    {"name": "Yogurt", "price": 1.79, "quantity": 4},
    {"name": "Bread", "price": 1.80, "quantity": 1},
    {"name": "Milk", "price": 1.59, "quantity": 2}
]

#C1
total = 0

for item in basket:
    total = total + item["price"] * item["quantity"]

print(f"Total: €{total:.2f}")

#C2
def print_receipt(basket):

    total = 0

    for item in basket:

        item_total = item["price"] * item["quantity"]

        total = total + item_total

        print(
            item["name"],
            item["quantity"],
            "x",
            f"€{item['price']:.2f}",
            f"€{item_total:.2f}"
        )

    print("------------------------------")
    print(f"Total €{total:.2f}")


print_receipt(basket)

#C3
def find_item(basket, item_name):

    for item in basket:
        if item["name"].lower() == item_name.lower():
            return item

    return None

result = find_item(basket, "Milk")
print(result)

#C4
def change_quantity(basket, item_name, new_quantity):

    if new_quantity < 0:
        return False

    for item in basket:

        if item["name"].lower() == item_name.lower():
            item["quantity"] = new_quantity
            return True

    return False

change_quantity(basket, "Milk", 5)

print(basket)

#C5
def calc_total(basket):

    total = 0

    for item in basket:
        total = total + item["price"] * item["quantity"]

    if total >= 50:
        discount = total * 0.10
        total = total - discount

    return total

print(f"€{calc_total(basket):.2f}")

#D1
#Display a question
#Get the user's answer
#Check the answer
#Keep track of the score
#Display the final result

#D2
def display_question(question):
    print(question)


def check_answer(answer, correct_answer):

    if answer.lower() == correct_answer.lower():
        return True
    else:
        return False


def display_result(score, num_questions):

    print("------------------------------")
    print("Quiz complete")
    print("Score:", score, "/", num_questions)
    print("------------------------------")


def run_quiz():

    questions = [
        {
            "question": "What is 2 + 2?",
            "answer": "4"
        },
        {
            "question": "What colour is the sky?",
            "answer": "blue"
        }
    ]

    score = 0

    for question in questions:

        display_question(question["question"])

        answer = input("Your answer: ")

        if check_answer(answer, question["answer"]):
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect.")

