class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        braces_dict = {
            '}': '{',
            ')': '(',
            ']':'['
            
        }
        opening = "({["
        closing = ")}]"
        if len(s) == 0:
            return True
        #else:
        res = True
        for elem in s:
            if elem in opening:
                mystack.insert(0,elem)
            elif elem in closing:
                if len(mystack) == 0:
                    return False
                if not braces_dict[elem] == mystack[0]:
                    res = False
                    break
                else:
                    mystack.pop(0)
        res = True if len(mystack) == 0 else False
        return res 


if __name__ == "__main__":
    print(Solution().isValid("[]"))