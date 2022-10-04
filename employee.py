"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Emp_Contract(Employee):
    def __init__(self, name, hours, rate, commission = None):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.commission = commission

    def get_pay(self):
        self.pay = 0
        if self.commission:
            self.pay += self.commission.get_amount()
        self.pay += self.hours * self.rate
        return self.pay

    def __str__(self):
        if self.commission:
            return (f'{self.name} works on a contract of {self.hours} at {self.rate}/hour{self.commission.get_string()} Their total pay is {self.pay}')
        else:
            return (f'{self.name} works on a contract of {self.hours} at {self.rate}/hour. Their total pay is {self.pay}')

class Emp_Salary(Employee):
    def __init__(self, name, salary, commission = None):
        super().__init__(name)
        self.salary = salary
        self.commission = commission

    def get_pay(self):
        self.pay = 0
        if self.commission:
            self.pay += self.commission.get_amount()
        self.pay += self.salary
        return self.pay

    def __str__(self):
        if self.commission:
            return (f'{self.name} works on a monthly salary of {self.salary}{self.commission.get_string()} Their total pay is {self.pay}')
        else:
            return (f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.pay}')


class Commission:
    def __init__(self, bonus=0, numb_contract=0, value=0):
        self.bonus = bonus
        self.numb_contract = numb_contract
        self.value = value

    def get_amount(self):
        self.total_bonus = 0
        if self.bonus:
            self.total_bonus += self.bonus
        if self.value and self.numb_contract:
            self.total_bonus = self.value * self.numb_contract
        return self.total_bonus

    def get_string(self):
        self.out = ""
        if self.bonus:
            self.out = (f" and receives a bonus commission of {str(self.bonus)}.")

        if self.value and self.numb_contract:
            self.out = (f" and receives a commission for {str(self.numb_contract)} contract(s) at {str(self.value)}/contract.")
        return self.out



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Emp_Salary("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Emp_Contract("Charlie", 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
r_comm = Commission(numb_contract = 4, value = 200)
renee = Emp_Salary("Renee", 3000, r_comm)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
j_comm = Commission(numb_contract = 3, value = 220)
jan = Emp_Contract("Jan", 150, 25, j_comm)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
rob_comm = Commission(bonus = 1500)
robbie = Emp_Salary("Robbie", 2000, rob_comm)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ar_comm = Commission(bonus = 600)
ariel = Emp_Contract("Ariel", 120, 30, ar_comm)
