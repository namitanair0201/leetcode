class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        opt = [[None for i in range(n)] for j in range(n)]
        res = []
        #setting base cases
        for i in range(n):
            for j in range(n):
                if i==j:
                    opt[i][j] = 1
                elif i == j + 1:
                    opt[i][j] = 0

        for i in range(n-1,-1,-1):
            for j in range(n):
                if i >= j:
                    continue
                #dp for upper triangle
                elif i < j:
                    if s[i] == s[j]:
                        opt[i][j] = opt[i+1][j-1] + 2
                    else:
                        opt[i][j] = max(opt[i+1][j], opt[i][j-1])
        return opt[0][n-1], res

if __name__ == "__main__":
    word = "boba"
    length, res = Solution().longestPalindrome(word)
    print(length, res)