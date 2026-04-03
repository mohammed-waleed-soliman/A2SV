# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        a = []
        b = []
        copy = head
        while head:
            if head.val<x:
                a.append(head.val)
            else:
                b.append(head.val)
            head = head.next
        for i in range(len(b)):
            a.append(b[i])
        res = ListNode(a[0])
        ret = res
        for i in range(1,len(a)):
            res.next = ListNode(a[i])
            res = res.next
        return ret