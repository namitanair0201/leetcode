import sys

class Solution:
    def maxSubArray(self, nums) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        elif n == 0:
            return 0
        
        else:
            global_max = nums[0]
            local_max = [0 for i in range(n)]
            local_max[0] = nums[0]
            for i in range(1,n):
                local_max[i] = max(local_max[i-1] + nums[i], nums[i])
                if local_max[i] > global_max:
                    global_max = local_max[i]
        return global_max
