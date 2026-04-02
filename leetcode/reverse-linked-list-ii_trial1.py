# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        a=[]
        while i<left:
            a.append(head.val)
            head=head.next
            i+=1
        b=[]
        while i<=right:
            b.append(head.val)
            head=head.next
            i+=1
        c=[]
        while head:
            c.append(head.val)
            head=head.next
            i+=1

        if len(a)==0:
            res = ListNode(b[-1])
            ret = res
            for i in range(len(b)-2,-1,-1):
                res.next=ListNode(b[i])
                res = res.next
            for i in range(len(c)):
                res.next=ListNode(c[i])
                res = res.next
            return ret
        else:
            res = ListNode(a[0])
            ret = res
            for i in range(1,len(a)):
                res.next=ListNode(a[i])
                res = res.next
            for i in range(len(b)-1,-1,-1):
                res.next=ListNode(b[i])
                res = res.next
            for i in range(len(c)):
                res.next=ListNode(c[i])
                res = res.next
            return ret