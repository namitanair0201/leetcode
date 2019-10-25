class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
                    [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ],
        rotate the input matrix in-place such that it becomes:
            [
            [7,4,1],
            [8,5,2],
            [9,6,3]
            ]
            """
        n= len(matrix)
        for i in range(n):
            for j in range(n):
                if i<j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()
   
if __name__ == "__main__":
    Solution().rotate([[1,2,3],[4,5,6,],[7,8,9]])