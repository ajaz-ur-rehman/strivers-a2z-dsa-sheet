# Write a function that takes an integer n and returns the list of the factorial numbers smaller than or equal to N.

# Example
# factorial_numbers(3) -> [1, 2, 3]
# factorial_numbers(6) -> [1, 2, 6]
# factorial_numbers(7) -> [1, 2, 6]

# Time complexity: O(n)
# Space complexity: O(n)

# How does it work?
# The function uses a helper function to generate the factorial numbers.
# The helper function takes two arguments: curr and i.
# curr is the current factorial number.
# i is the current number.
# The helper function returns an empty list if curr is greater than n.
# Otherwise, it returns a list containing curr and the result of calling the helper function with curr * i and i + 1.
# The function calls the helper function with 1 and 1 and returns the result without the first element.


def factorial_numbers(n: int) -> list[int]:
    if n == 0:
        return []
        
    def next_factorial(curr: int, i: int) -> list[int]:
        if curr > n:
            return []
        
        return [curr] + next_factorial(curr * i, i + 1)
        
    return next_factorial(1, 1)[1:]