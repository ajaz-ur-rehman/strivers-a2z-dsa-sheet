# Write a function that takes an integer n and returns the number of digits in n.

# Example
# count_digits(123) -> 3

# Time complexity: O(1)
# Space complexity: O(1)

import math

def count_digits(n: int) -> int:
    count = int(math.log10(n) + 1)

    return count