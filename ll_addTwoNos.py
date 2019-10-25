#Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = current = ListNode(0)
        
        carry = 0
        while(l1!=None or l2!=None or carry!=0):
            sum = 0
            if l1 :
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum += l2.val
                l2 = l2.next
            carry, current.val = divmod( carry + sum , 10 )
            current.next = ListNode(None)
            current = current.next
        return result

if __name__ == "__main__":
    l1 = ListNode(9)
    l1.next = ListNode(7)
    l2= ListNode(8)
    l2.next=ListNode(6)
    t1 = Solution().addTwoNumbers(l1,l2)