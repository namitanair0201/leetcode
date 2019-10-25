import numpy as np

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = np.array(grid)
        max_in_col = np.max(grid, 0)
        max_in_row  = np.max(grid, 1)
        sum = 0
        it = np.nditer(grid, )
        width = len(grid[0])

        for i in range(width):
            for j in range(width):
                replacement = sorted([max_in_col[j],max_in_row[i],grid[i][j]])[1]
                sum +=  replacement - grid[i][j]
                grid[i][j] = replacement
        print(grid)
        return sum

if __name__ == "__main__":
    my_grid = [ [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0] ]
    print("input is ", my_grid)
    print("expected is [8, 4, 8, 7],[7, 4, 7, 7],[9, 4, 8, 7],[3, 3, 3, 3] ]")
    test = Solution().maxIncreaseKeepingSkyline(my_grid) 
    print("received is ",test)