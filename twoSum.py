#hash map efficient solution

class Solution(object):
    def twoSum(self, num_list, target):
        dic = {} #initializing empty dictionary
        for index,num in enumerate(num_list):
            num2 = target-num
            if num2 not in dic :
                dic[num] = index #creating the reverse map ie value = key
            else:
                return [index, dic[num2]]
        
test = Solution()
print(test.twoSum([0,1,2,3,],4))
    








# first solution
# class Solution(object):
#     def twoSum(self, num_list, target):
#         for num1 in num_list:
#             num2 = target - num1
#             first_index = num_list.index(num1) #storing the index of first number
#             num_list[first_index] = None #so that it does not repeat index

#             if num2 in num_list: #checking if num1 and num2 will be a match 
#                 second_index = num_list.index(num2)
#                 return [first_index, second_index]

# test = Solution()
# print(test.twoSum([0,2,3,0],0))
