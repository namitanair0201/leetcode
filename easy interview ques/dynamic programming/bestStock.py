from sys import maxsize

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        
        if n == 0:
            return 0
        
        elif n == 1:
            return 0
        
        else:
            min_price = maxsize
            maxprofit = 0
            for i in range(n):
                if prices[i] < min_price:
                    min_price = prices[i]
                elif prices[i] - min_price > maxprofit:
                    maxprofit = prices[i] - min_price
            return maxprofit

            
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))