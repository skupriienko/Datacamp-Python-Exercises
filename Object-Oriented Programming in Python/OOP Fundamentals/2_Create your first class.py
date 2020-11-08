# Include a set_name method
class Employee:

    def set_name(self, new_name):
        self.name = new_name

    # Add set_salary() method

    def set_salary(self, new_salary):
        self.salary = new_salary


# Create an object emp of class Employee
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)


# Set the salary of emp to 50000
emp.set_salary(50000)
