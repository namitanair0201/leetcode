class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        _dict = { 'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        prev = 0
        num=0
        for digit in s[::-1]:
            current = _dict[digit]
            if prev > current:
                num -= current
            else:
                num += current
            prev = current
        return num
