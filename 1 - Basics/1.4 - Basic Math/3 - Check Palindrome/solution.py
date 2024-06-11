# Write a function that checks if a given integer is a palindrome without using strings.

# Example
# isPalindrome(121) -> True
# isPalindrome(-121) -> False
# isPalindrome(10) -> False

# Time complexity: O(log(n))
# Space complexity: O(1)

# How does it work?
# The function first checks if the input number is 0, negative, or divisible by 10.
# If the number is 0, the function returns True.
# If the number is negative or divisible by 10, the function returns False.

# The function then initializes a variable 'rev' to 0.
# It enters a while loop that continues until the input number is greater than 'rev'.

# In each iteration, the function calculates the quotient and remainder of the input number divided by 10.
# The quotient is stored in the input number, while the remainder is appended to 'rev'.
# This process effectively reverses the second half of the input number.

# If the input number is equal to 'rev' or 'rev' divided by 10, the function returns True.
# Otherwise, it returns False.

# We are using 'rev' divided by 10 to handle odd-length palindromes to disregard the middle digit.

def isPalindrome(x: int) -> bool:
    if x == 0:
        return True
    elif x < 0 or x % 10 == 0:
        return False
    
    rev = 0

    while x > rev:
        x, mod = divmod(x, 10)
        rev = rev * 10 + mod

    return x == rev or x == rev // 10