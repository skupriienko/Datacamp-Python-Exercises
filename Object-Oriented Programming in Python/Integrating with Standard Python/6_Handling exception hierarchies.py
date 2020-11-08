class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary = 30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")

        elif self.salary + amount <  Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")

        else:
            self.salary += amount

# emp = Employee("Katze Rik", salary=50000)
# try:
#     emp.give_bonus(7000)
# except SalaryError:
#     print("SalaryError caught!")

# try:
#     emp.give_bonus(7000)
# except BonusError:
#     print("BonusError caught!")

# try:
#     emp.give_bonus(-100000)
# except SalaryError:
#     print("SalaryError caught again!")

# try:
#     emp.give_bonus(-100000)
# except BonusError:
#     print("BonusError caught again!")

emp = Employee("Katze Rik",\
                    50000)
try:
    emp.give_bonus(7000)
except SalaryError:
    print("SalaryError caught")
except BonusError:
    print("BonusError caught")

emp = Employee("Katze Rik",\
                    50000)
try:
    emp.give_bonus(7000)
except BonusError:
    print("BonusError caught")
except SalaryError:
    print("SalaryError caught")
