"""Probabilities and Statistics
Choosing a President, Vice President, and Secretary
You have a group of 12 people , and you need to elect 3 distinct positions"""


# first we know that order matters in this case, so we can use permutations to calculate 
# the number of ways to choose 3 distinct positions from 12 people.

# Second, we know also that does not replasment in this case.

# Third the formula for this is given by P(n,r) = n! / (n - r)!

# P(12, 3) = 12*11*10 = 1320

def factorial(n: int) -> int:
    """Calclulate the factorial of number n."""
    if n == 0 or n ==1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

factorial_12 = factorial(12)
factorial_9 = factorial(9)

def permutations(n: int, r: int) -> int:
    return factorial(n) // factorial(n - r)

# print(f"P(12, 3) = {permutations(12, 3)}")

print(f"Factorial of 12 is: {factorial_12}")
print(f"Factorial of 9 is: {factorial_9}")
print(f"Permutations of 12 taken 3 at a time is: {permutations(12, 3)}")

print(f"P(12, 3) = {permutations(12, 3)}")
