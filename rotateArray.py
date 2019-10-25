#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r = k % len(nums)
        if r!=0 and len(nums)!= 1:
            nums[:] = nums[-r:]+ nums[:len(nums) - r]

        #approach 2
        # size = len(nums)
        # for i in range(k):
        #     temp = nums[size-1]
        #     for j in range(size-1,0,-1):
        #         nums[j] = nums[j-1]
        #     nums[0] = temp
