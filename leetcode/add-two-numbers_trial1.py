# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        x = 0
        y = 0
        for i in range(len(a)-1,-1,-1):
            x*=10
            x+=a[i]
        for i in range(len(b)-1,-1,-1):
            y*=10
            y+=b[i]
        res = x+y
        ret = ListNode(res%10)
        res//=10
        copy = ret
        while res:
            ret.next=ListNode(res%10)
            ret = ret.next
            res//=10
        return copy