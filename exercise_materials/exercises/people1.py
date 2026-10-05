class Employee:

    def __init__(self, id, first_name="", last_name="", salary=0, job_title=""):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self._salary = salary
        self.job_title = job_title

    def get_salary(self):
        return self._salary

    def display(self):
        print("Employee[ id:", self.id,
              ", first name:", self.first_name,
              ", last name:", self.last_name,
              ", salary:", self._salary, "]")

    def calc_net_pay(self):

        tax = self._salary * 0.42

        yearly_pay = self._salary - tax

        monthly_pay = yearly_pay / 12

        return monthly_pay

    def calc_bonus(self):

        if "manager" in self.job_title.lower():
            bonus = self._salary * 0.15

        elif "intern" in self.job_title.lower():
            bonus = self._salary * 0.02

        else:
            bonus = self._salary * 0.06

        return bonus

