class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s if x.isalnum()]
        rev = s[::-1]
        return rev == s