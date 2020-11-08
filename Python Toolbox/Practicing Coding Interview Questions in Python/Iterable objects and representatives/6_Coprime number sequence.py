list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
list2 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

def gcd(a, b):
    # Define the while loop as described
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b
    # Complete the return statement
    return a

# Create a list of tuples defining pairs of coprime numbers
coprimes = [(i, j) for i in list1
                   for j in list2 if gcd(i, j) == 1]
print(coprimes)
