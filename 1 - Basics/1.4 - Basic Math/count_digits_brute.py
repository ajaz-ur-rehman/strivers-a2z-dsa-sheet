# Write a function that takes an integer n and returns the number of digits in n.

# Example
# count_digits(123) -> 3

# Time complexity: O(log(n))
# Space complexity: O(1)

# How does it work?
# The function iteratively divides 'n' by 10
# and increments a counter until 'n' is 0.
# The counter is then returned as the result.

def count_digits(n: int) -> int:
    count = 0

    while n > 0:
        n //= 10
        count += 1

    return count
