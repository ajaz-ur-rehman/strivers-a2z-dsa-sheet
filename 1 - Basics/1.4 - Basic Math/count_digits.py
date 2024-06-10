# Write a function that takes an integer n and returns the number of digits in n.

# Example
# count_digits(123) -> 3

# Time complexity: O(log(n))
# Space complexity: O(1)

def count_digits(n: int) -> int:
    """Returns the number of digits in n.
    
    Args:
    n: int - The integer to count the digits of.
    
    Returns:
    int - The number of digits in n.
    """

    count = 0

    while n > 0:
        n //= 10
        count += 1

    return count
