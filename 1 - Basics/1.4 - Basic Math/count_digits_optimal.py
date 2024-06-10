# Write a function that takes an integer n and returns the number of digits in n.

# Example
# count_digits(123) -> 3

# Time complexity: O(1)
# Space complexity: O(1)

# How does it work?
# The expression int(math.log10(n) + 1)
# calculates the number of digits in 'n'
# and casts it to an integer.

# Adding 1 to the result accounts
# for the case when 'n' is a power of 10,
# ensuring that the count is correct.

# Finally, the result is cast
# to an integer to ensure it is rounded
# down to the nearest whole number.

import math

def count_digits(n: int) -> int:
    count = int(math.log10(n) + 1)

    return count