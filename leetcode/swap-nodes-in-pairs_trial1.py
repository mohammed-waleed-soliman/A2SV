# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        for i in range(0,len(temp),2):
            if i+1==len(temp):
                break
            x = temp[i]
            temp[i]=temp[i+1]
            temp[i+1]=x
        ret = None
        if len(temp)!=0:
            res = ListNode(temp[0])
            ret = res
            for i in range(1,len(temp)):
                res.next = ListNode(temp[i])
                res = res.next
        return ret