# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        n = root
        def dfs(node):
            if not node:
                return
            nonlocal n
            if node.val==val:
                n = node
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        if n.val!=val:
            return None
        return n