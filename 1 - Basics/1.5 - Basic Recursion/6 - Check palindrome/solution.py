# Write a function that checks if a string is a palindrome using recursion. The function should ignore spaces, punctuation, and capitalization.

# Example
# is_palindrome("A man, a plan, a canal: Panama") -> True
# is_palindrome("race a car") -> False
# is_palindrome(" ") -> True

# Time complexity: O(n)
# Space complexity: O(n)

# How does it work?
# The function uses a helper function to check if the string is a palindrome.
# The helper function takes two arguments: left and right.
# left is the index of the left character.
# right is the index of the right character.
# The helper function returns True if left is greater than right.
# The helper function returns the result of calling itself with left + 1 and right if the left character is not alphanumeric.
# The helper function returns the result of calling itself with left and right - 1 if the right character is not alphanumeric.
# The helper function returns False if the left and right characters are different.
# The helper function returns the result of calling itself with left + 1 and right - 1 if the left and right characters are the same.
# The function calls the helper function with 0 and the length of the string - 1.

def is_palindrome(s: str) -> bool:
    def check_pal(left: int, right: int) -> bool:
        if left > right:
            return True

        if not s[left].isalnum():
            return check_pal(left + 1, right)
        elif not s[right].isalnum():
            return check_pal(left, right - 1)
        elif s[left].lower() != s[right].lower():
            return False
        else:
            return check_pal(left + 1, right - 1)

    return check_pal(0, len(s) - 1)