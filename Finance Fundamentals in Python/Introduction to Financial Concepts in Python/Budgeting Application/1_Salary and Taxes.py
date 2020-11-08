# Enter your annual salary
salary = 85000

# Assume a tax rate of 30%
tax_rate = 0.3

# Calculate your salary after taxes
salary_after_taxes = salary * (1 - 0.3)
print("Salary after taxes: " + str(round(salary_after_taxes, 2)))

# Calculate your monthly salary after taxes
monthly_takehome_salary = salary_after_taxes /12
print("Monthly takehome salary: " + str(round(monthly_takehome_salary, 2)))
