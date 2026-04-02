# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        copy = head
        while copy:
            sz+=1
            copy=copy.next
        n = sz-n+1
        a=[]
        i = 1
        while head:
            if i!=n:
                a.append(head.val)
            head=head.next
            i+=1
        if len(a)==0:
            return head
        res=ListNode(a[0])
        ret = res
        for i in range(1,len(a)):
            res.next=ListNode(a[i])
            res = res.next
        return ret