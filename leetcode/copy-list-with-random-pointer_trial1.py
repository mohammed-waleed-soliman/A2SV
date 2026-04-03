"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        copy = head
        mp = {}
        i = 0
        while head:
            mp[head]=i
            head=head.next
            i+=1
        head = copy
        res = Node(head.val)
        ret = res
        m={}
        i = 0
        m[i]=res
        while head:
            if head.next:
                res.next = Node(head.next.val)
                i+=1
                m[i]=res.next
                res = res.next
                head = head.next
            else:
                break
        head = copy
        res = ret
        while head:
            if head.random:
                ind = mp[head.random]
                res.random = m[ind]
            head = head.next
            res = res.next
        return ret