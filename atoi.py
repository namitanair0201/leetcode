from math import floor
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.replace(" ", '')
        digits = "+-0123456789"
        num = ""
        if s[0] not in digits:
            return 0
        else:
            num += s[0]
            for char in s[1:]:
                if char=='.':
                    break
                elif char.isnumeric():
                    num += char            
        if int(num) in range(- 2**31, 2**31):
            return int(num)
        else:
            return -2**31

if __name__ == "__main__":
    print(Solution().myAtoi(""))
