# Write a function that returns the n-th number in the Fibonacci sequence using recursion.

# Example
# fib(0) -> 0
# fib(1) -> 1
# fib(2) -> 1
# fib(3) -> 2
# fib(4) -> 3
# fib(5) -> 5

# Time complexity: O(n)
# Space complexity: O(n)

# How does it work?
# The function uses a helper function to calculate the n-th Fibonacci number.
# The helper function takes one argument: n.
# The helper function returns n if n is less than or equal to 1.
# The helper function calculates the n-th Fibonacci number if n is not in the cache.
# The helper function stores the result in the cache.
# The helper function returns the result.
# The function calls the helper function with n.

def fib(n: int) -> int:
    cache = {}

    def calc_fib(n: int) -> int:
        if n <= 1:
            return n

        if n not in cache:
            cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
        
        return cache[n]

    return calc_fib(n)