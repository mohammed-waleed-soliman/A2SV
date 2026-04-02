# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a = []
        while head:
            if head.val!=val:
                a.append(head.val)
            head=head.next
        if len(a)==0:
            return head
        res = ListNode(a[0])
        ret = res
        for i in range(1,len(a)):
            res.next = ListNode(a[i])
            res = res.next
        return ret