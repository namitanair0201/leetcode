class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = {}
        result = []

        for digit in nums1:
            counter[digit] = counter.get(digit,0)+1

        for digit in nums2:
            if counter.get(digit,0) > 0:
                result += [digit] 
                counter[digit] -= 1
        return result