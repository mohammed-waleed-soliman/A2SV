# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        copy = head
        while copy:
            size+=1
            copy=copy.next
        ind = size//2
        i = 0
        while i<ind:
            i+=1
            head=head.next
        return head