#array is sorted
#index1 < index2
#index starts from 1 and not 0

class Solution:
    def twoSum2(self, numbers, target):
        """
        Input: numbers = [2,7,11,15], target = 9
            Output: [1,2]
            Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
        """
        start = 0
        end = len(numbers)-1
        #binary search
        while(start<=end):
            if numbers[start]+numbers[end]<target:
                start+=1
            elif numbers[start]+numbers[end]>target:
                end-=1
            else:
                return[start+1, end+1]

test = Solution()
print(test.twoSum2([1,2,3,4],4))