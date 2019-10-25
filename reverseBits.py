class Solution:
    def reverseBits(self, n):
        temp = str(n)
        return "".join(reversed(temp))

test = Solution().reverseBits('00000010100101000001111010011100')
print(test)