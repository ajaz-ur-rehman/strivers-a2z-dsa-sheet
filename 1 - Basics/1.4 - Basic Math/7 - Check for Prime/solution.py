# Write a function that takes an integer as input and returns True if the number is prime and False if it is not.

# Example
# isPrime(5) -> True
# isPrime(6) -> False

# Time complexity: O(sqrt(n))
# Space complexity: O(1)

# How does it work?
# The function returns False if the number is less than or equal to 1.
# The function iterates from 2 to the square root of the number.
# If the number is divisible by any number in the range, the function returns False.
# Otherwise, the function returns True.

from math import sqrt 

def is_prime(n: int) -> bool:
    if (n <= 1): 
        return False
    
    for i in range(2, int(sqrt(n))+1): 
        if (n % i == 0): 
            return False
  
    return True