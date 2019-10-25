#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+= prices[i+1]- prices[i]
        return profit

if __name__ == "__main__":
    print(Solution().maxProfit([7,6,4,3,1]))

