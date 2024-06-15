# Write a function that returns the sum of the first n terms of the series 1^3 + 2^3 + 3^3 + ... + n^3.

# Example
# sum_of_series(3) -> 36
# sum_of_series(5) -> 225
# sum_of_series(7) -> 784

# Time complexity: O(1)
# Space complexity: O(1)

# How does it work?
# The function uses the formula for the sum of the first n natural numbers to calculate the sum of the first n cubes.
# The formula for the sum of the first n natural numbers is n * (n + 1) / 2.
# The function squares the result to get the sum of the first n cubes.
# The function returns the result.

def sum_of_series(n: int) -> int:
    return (n * (n + 1) // 2) ** 2