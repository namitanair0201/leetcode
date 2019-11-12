class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0 for i in range(n)]
        if n == 1:
            return 1
        elif n ==2:
            return 2
        elif n > 2:
            count[0] = 1
            count[1] = 2
            for i in range(2,n):
                count[i] = (count[i-1] + count[i-2])
        return count[n-1]

if __name__ == "__main__":
    print(Solution().climbStairs(100))