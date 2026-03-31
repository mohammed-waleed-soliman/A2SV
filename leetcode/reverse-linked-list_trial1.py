# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        temp=[]
        while head:
            temp.append(head.val)
            head=head.next
        temp.reverse()
        res = ListNode(temp[0])
        cur = res
        for i in range(1,len(temp)):
            cur.next=ListNode(temp[i])
            cur=cur.next
        return res