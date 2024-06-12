# Write a function that takes an integer and returns True if it is an Armstrong number, and False otherwise.
# An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

# Example
# is_armstrong_number(153) -> True
# is_armstrong_number(123) -> False
# is_armstrong_number(0) -> True

# Time complexity: O(log(n))
# Space complexity: O(1)

# How does it work?
# The function first calculates the number of digits in the input number.
# It then initializes two variables, 'total' and 'x', to 0 and the input number, respectively.

# The function enters a while loop that continues until 'x' is 0.
# In each iteration, the function calculates the quotient and remainder of 'x' divided by 10.
# The remainder is raised to the power of the number of digits and added to 'total'.

# Finally, the function returns True if 'total' is equal to the input number, and False otherwise.

import math

def is_armstrong_number(n: int) -> bool:
    digits = int(math.log10(n) + 1)
    total = 0
    x = n
    
    while x:
        x, mod = divmod(x, 10)
        total += mod ** digits
        
    return total == n