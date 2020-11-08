from math import sqrt

cands = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]

def is_prime(n):
    # Define the initial check
    if n < 2:
        return False
    # Define the loop checking if a number is not prime
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num)]
print("primes = " + str(primes))
