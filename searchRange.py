class Solution:
    def searchRange(self, nums, target):
        result =[]
        res_found = False
        n = len(nums)
        beg = 0
        end = n-1

        #when the length of array is 1
        if n == 1 and nums[0] == target:
            return [0,0]
        elif n == 1 and nums[0] != target:
            return [-1,-1]

        #when the length of array is 2
        while n >1 and beg <= end and res_found == False:

            middle = (beg+end)//2
            
            #when the number is found
            if nums[middle] == target:
                res_found = True

                #checking if element repeats before middle
                for i in range(middle,-1,-1):
                    if not nums[i] == target:
                        break
                if i != 0 :
                    result.append(i+1)
                else:
                    result.append(i)
                #checking numbers after middle
                for i in range(middle, n):
                    if not nums[i] == target:
                        break
                if i == n-1:
                    result.append(i)
                else:
                    result.append(i-1)

            elif nums[middle] < target:
                beg = middle +1

            elif nums[middle] > target:
                end = middle -1
        
        if res_found:
            return result
        elif not res_found:
            return [-1,-1]

if __name__ == "__main__":
    print(Solution().searchRange([2,2],2))