class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 0:
            return 0
        elif n == 1:
            return 0
        else:
            opt = [0 for i in range(n)]
            max_profit = 0
            for i in range(1,n):
                for j in range(i):
                    if prices[j]< prices[i]:
                        max_profit = max( max_profit, prices[i]-prices[j])
                    opt[i] = max(max_profit, opt[i-1])
            return opt[n-1]

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))