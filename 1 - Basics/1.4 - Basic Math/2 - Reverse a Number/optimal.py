# Write a function that takes an integer as input and returns the integer reversed.

# Example
# reverse(123) -> 321
# reverse(-123) -> -321

# Time complexity: O(log(n))
# Space complexity: O(1)

# How does it work?
# The function first determines the sign of the input number.
# It then initializes two variables, 'rev' and 'n'.

# The 'rev' variable will store the reversed number,
# while the 'n' variable will store the absolute value of the input Wnumber.

# The function then enters a while loop that continues until 'n' is 0.
# In each iteration, the function calculates the quotient and remainder of 'n' divided by 10.

# The quotient is stored in 'n', while the remainder is appended to 'rev'.
# This process effectively reverses the number.

# If the reversed number exceeds the 32-bit signed integer limit,
# the function returns 0.

# Finally, the function returns the reversed number multiplied by the sign of the input number.

def reverse(x: int) -> int:
    sign = [1, -1][x < 0]
    rev, n = 0, abs(x)

    while n:
        n, mod = divmod(n, 10)
        rev = rev * 10 + mod

        if rev > 2 ** 31 - 1:
            return 0

    return rev * sign
    