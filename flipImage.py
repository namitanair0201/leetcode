
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = [list(reversed(row)) for row in A]
        A[:] = [[abs(1-elem) for elem in row] for row in A]

