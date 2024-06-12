# Write a function that computes the greatest common divisor of two numbers.

# Example
# computeGcd(8, 12) -> 4
# computeGcd(100, 200) -> 100
# computeGcd(7, 5) -> 1

# Time complexity: O(log(min(x, y)))
# Space complexity: O(1)

# How does it work?
# The function uses the Euclidean algorithm to compute the greatest common divisor of two numbers.
# The algorithm states that the GCD of two numbers is the same as the GCD of the smaller number and the remainder of the larger number divided by the smaller number.
# The function iterates through the numbers until the second number becomes 0.
# In each iteration, the function swaps the numbers and calculates the remainder of the division.
# The function returns the first number when the second number becomes 0.

def computeGcd(x, y):
    while y:
        x, y = y, x % y
    
    return x
    