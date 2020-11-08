class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    # Add a constructor
    def __init__(self, name, salary=50000, project=None):

        # Call the parent's constructor
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project

    def display(self):
        print("Manager ", self.name)
