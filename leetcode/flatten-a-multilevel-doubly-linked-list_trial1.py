"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    temp = []
    def dfs(self, head: 'Optional[Node]') -> 'Optional[Node]':
        while head:
            self.temp.append(head.val)
            if head.child:
                self.dfs(head.child)
            head = head.next
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(head)
        print(self.temp)
        if len(self.temp)==0:
            return None
        res = Node(self.temp[0],None,None,None)
        copy = res
        for i in range(1,len(self.temp)):
            res.next = Node(self.temp[i],res,None,None)
            res = res.next
        self.temp.clear()
        return copy