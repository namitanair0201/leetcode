class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 0:
            return 0
        
        elif n == 1:
            return nums[0]

        else:    
            opt = [0 for i in range(n)]
            opt[0] = nums[0]
            opt[1] = nums[0] if nums[0] > nums[1] else nums[1]
            for i in range(2,n):
                opt[i] = max( nums[i] + opt[i-2], opt[i-1])
        return opt[n-1]