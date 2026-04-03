# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        if len(a)==0:
            return head
        a.sort()
        res=ListNode(a[0])
        ret = res
        for i in range(1,len(a)):
            if a[i]!=a[i-1]:
                res.next = ListNode(a[i])
                res = res.next
        return ret