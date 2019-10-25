class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        [9,9,9] = [1,0,0,0]
        """
        carry=1
        num = 0

        for i in range(len(digits)-1,-1,-1):
            num = ( digits[i] + carry ) % 10
            carry = ( digits[i] + carry ) // 10
            digits[i] = num
        if carry != 0:
            digits.insert(0,carry)
        return digits

