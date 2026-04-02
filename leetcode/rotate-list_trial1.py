# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        if len(a)==0:
            return head
        k %= len(a)
        b = []
        for i in range(len(a)-k,len(a)):
            b.append(a[i])
        for i in range(len(a)-k):
            b.append(a[i])
        res = ListNode(b[0])
        ret = res
        for i in range(1,len(b)):
            res.next=ListNode(b[i])
            res=res.next
        return ret