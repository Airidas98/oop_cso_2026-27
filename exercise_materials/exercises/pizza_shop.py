
from pizza_orders import Pizza
from datetime import datetime

order = {}

username = input("Enter your username: ")

while True:
    answer = input("Do you want to order a pizza? (yes/no): ").lower()

    if answer != "yes":
        break

    nickname = input("Enter a nickname for your pizza: ")

    while nickname in order or nickname == "":
        print("Nickname already used or empty. Try again.")
        nickname = input("Enter a nickname for your pizza: ")

    size = input("Enter pizza size: ")

    toppings = []

    while True:
        topping = input("Enter a topping or press Enter to finish: ")

        if topping == "":
            break

        toppings.append(topping)

    if len(toppings) == 0:
        toppings = ["Tomato sauce", "Cheese"]

    pizza = Pizza(toppings, size)

    order[nickname] = pizza

    print("Your pizza:")
    pizza.display()
    print("Price: €", format(pizza.calc_price(), ".2f"))

if len(order) > 0:

    total = 0
    highest_price = 0
    expensive_name = ""

    print("\nYour complete order:")

    for nickname in order:
        pizza = order[nickname]

        print("\nNickname:", nickname)
        pizza.display()

        price = pizza.calc_price()
        print("Price: €", format(price, ".2f"))

        total = total + price

        if price > highest_price:
            highest_price = price
            expensive_name = nickname

    print("\nMost expensive pizza:")
    order[expensive_name].display()
    print("Price: €", format(highest_price, ".2f"))

    print("\nTotal bill: €", format(total, ".2f"))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = username + "_" + timestamp + ".txt"

    with open(filename, "w") as file:
        file.write("Pizza order for " + username + "\n")

        for nickname in order:
            pizza = order[nickname]

            file.write("\nNickname: " + nickname + "\n")
            file.write("Size: " + pizza.get_size() + "\n")
            file.write("Price: €" + format(pizza.calc_price(), ".2f") + "\n")

        file.write("\nTotal bill: €" + format(total, ".2f"))

    print("Order saved to", filename)

else:
    print("No pizzas ordered.")

