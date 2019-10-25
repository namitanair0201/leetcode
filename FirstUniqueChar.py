import math
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, char in enumerate(s):
            if char in dic:
                dic[char] = math.inf
            else:
                dic[char]= i
        print(dic)
        indices = sorted(list(dic.values()))
        print(indices)
        if indices and indices[0] != math.inf:
            return indices[0]
        else:
            return -1
