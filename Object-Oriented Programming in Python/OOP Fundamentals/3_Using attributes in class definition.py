class Employee:
  def set_name(self, new_name):
    self.name = new_name

  def set_salary(self, new_salary):
    self.salary = new_salary

emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)
