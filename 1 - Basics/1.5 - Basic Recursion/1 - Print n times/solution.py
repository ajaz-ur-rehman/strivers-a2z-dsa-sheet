# Write a recursive function that takes an integer N as input and prints the numbers from 1 to N.

# Example
# printNos(5) -> 1 2 3 4 5
# printNos(3) -> 1 2 3
# printNos(1) -> 1

# Time complexity: O(N)
# Space complexity: O(N)

# How does it work?
# The function uses recursion to print the numbers from 1 to N.
# The function calls itself with N - 1 until N becomes 0.
# The function prints the number after the recursive call.

def printNos(N: int) -> None:
    if N > 0:
        printNos(N - 1)
        print(N, end=" ")