from people1 import Employee


employees = {}


# Create 3 employees
for i in range(3):

    print()
    print("Employee", i + 1)

    # Get employee ID
    employee_id = int(input("Enter employee ID: "))

    # Check if ID already exists
    while employee_id in employees:

        print("ID already exists.")

        employee_id = int(input("Enter another employee ID: "))

    # Get employee details
    first_name = input("Enter first name: ")

    last_name = input("Enter last name: ")

    salary = float(input("Enter salary: "))

    job_title = input("Enter job title: ")

    # Create Employee
    employee = Employee(
        employee_id,
        first_name,
        last_name,
        salary,
        job_title
    )

    # Add Employee to dictionary
    employees[employee_id] = employee


# Find lowest net pay
lowest_employee = None
lowest_pay = 0


for employee in employees.values():

    pay = employee.calc_net_pay()

    if lowest_employee is None or pay < lowest_pay:

        lowest_employee = employee
        lowest_pay = pay


# Find highest bonus
highest_employee = None
highest_bonus = 0


for employee in employees.values():

    bonus = employee.calc_bonus()

    if highest_employee is None or bonus > highest_bonus:

        highest_employee = employee
        highest_bonus = bonus


# Display lowest net pay employee
print()
print("Employee with lowest net pay:")

lowest_employee.display()

print("Monthly net pay:", round(lowest_pay, 2))


# Display highest bonus employee
print()
print("Employee with highest bonus:")

highest_employee.display()

print("Bonus:", round(highest_bonus, 2))