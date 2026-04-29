# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = [val]
        def dfs(node):
            if not node:
                return
            temp.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        temp.sort()
        if not root:
            root = TreeNode(temp[0])
        else:
            root.val=temp[0]
        root.left=None
        ch = root
        for i in range(1,len(temp)):
            ch.right=TreeNode(temp[i])
            ch = ch.right
        return root