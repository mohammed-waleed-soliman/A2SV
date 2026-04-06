# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        mx = 0
        for i in range(len(temp)//2):
            mx = max(mx,temp[i]+temp[len(temp)-1-i])
        return mx