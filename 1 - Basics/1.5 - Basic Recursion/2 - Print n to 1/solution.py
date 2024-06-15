# Write a recursive function that takes an integer N as input and prints the numbers from N to 1.

# Example
# printNos(5) -> 5 4 3 2 1
# printNos(3) -> 3 2 1
# printNos(1) -> 1

# Time complexity: O(N)
# Space complexity: O(N)

# How does it work?
# The function uses recursion to print the numbers from N to 1.
# The function prints the number before the recursive call.
# The function calls itself with N - 1 until N becomes 0.

def printNos(n: int) -> None:
    if n > 0:
        print(n, end=" ")
        printNos(n - 1)