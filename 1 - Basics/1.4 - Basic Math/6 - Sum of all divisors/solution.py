# Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined as the sum of all divisors of i.

# Example
# sumOfDivisors(4) -> 15
# sumOfDivisors(5) -> 21

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# The function initializes a variable 'total' to 0.
# It then iterates from 1 to N and calculates the sum of divisors for each number.
# The sum of divisors is calculated by iterating from 1 to N and adding i * (N // i) to the total.
# Finally, the function returns the total sum of divisors.

def sum_of_divisors(n: int) -> int:
    total = 0
    
    for i in range(1, n + 1):
        total += i * (n // i)
        
    return total