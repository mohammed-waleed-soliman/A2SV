# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        copy = head
        while head:
            size+=1
            head = head.next
        print(size)
        res = []
        rem = size%k
        sz = size//k
        head = copy
        for i in range(k):
            temp = []
            if rem!=0:
                for j in range(sz+1):
                    temp.append(head.val)
                    head = head.next
                rem-=1
            else:
                for j in range(sz):
                    temp.append(head.val)
                    head = head.next
            if len(temp)!=0:
                r = ListNode(temp[0])
                dummy = r
                for j in range(1,len(temp)):
                    r.next = ListNode(temp[j])
                    r = r.next
                res.append(dummy)
            else:
                res.append(None)
        return res