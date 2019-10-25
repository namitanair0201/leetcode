class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums[:] = [x for x in nums if x != val]
        # return len(nums)

        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        i=-1
        c=len(nums)
        while i<c:
            i+=1
            print(nums[i],i,c)
            if nums[i]==val:
                if i > 0 and i < c-1 :
                    nums[:] = nums[0:i-1]+nums[i+1:]
                if i == 0:
                    nums[:] = nums[1:]
                if i == c-1:
                    nums[:] = nums[:-1]
                c -= 1
        return c
if __name__ == "__main__":
    test = Solution().removeElement([1,2,3,4,4], 4)
    print(test)