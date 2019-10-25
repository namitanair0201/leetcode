class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_unique = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c!= '.':
                    check_unique += [(i,c), (c,j), (i//3, j//3, c)]
        return len(check_unique) == len(set(check_unique))