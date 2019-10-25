class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = "".join(reversed(str(x)))
        print(rev)
        if rev==str(x):
            return True
        else:
            return aFalse
        
print(Solution().isPalindrome(121))