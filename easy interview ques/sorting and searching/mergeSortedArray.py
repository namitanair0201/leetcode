class Solution:
    def merge(self, nums1 , m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 1 and n == 1:
            if nums1[0] < nums2[0]:
                nums1.insert(1,nums2[0])
            else:
                nums1.insert(0, nums2[0])
            del nums1[2]
            return nums1
        
        #delete the last 0 elements of the array
        del nums1[m:]

        i = 0
        j = 0
        
        while j < n and i < m:
            if j < n:
                print ("increment j")
            if i < m:
                print("incrememnt m")
            if nums1[i] < nums2[j]:
                i += 1
                print("first case")
                
            elif nums2[j] >= nums1[i]:
                nums1.insert(i, nums2[j] )
                j += 1
                print("second case")
        if j < n:
            nums1[:] = nums1 + nums2[j:] 
            print("here")
        return nums1    


if __name__ == "__main__":
    print(Solution().merge([4,5,6,0,0,0],3, [1,2,3,],3))