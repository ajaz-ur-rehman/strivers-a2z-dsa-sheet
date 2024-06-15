# Write a recursive function that takes an integer N as input and prints the numbers from 1 to N.

# Example
# print_nos(5) -> 1 2 3 4 5
# print_nos(3) -> 1 2 3
# print_nos(1) -> 1

# Time complexity: O(N)
# Space complexity: O(N)

# How does it work?
# The function uses recursion to print the numbers from 1 to N.
# The function calls itself with N - 1 until N becomes 0.
# The function prints the number after the recursive call.

def print_nos(n: int) -> None:
    if n > 0:
        print_nos(n - 1)
        print(n, end=" ")