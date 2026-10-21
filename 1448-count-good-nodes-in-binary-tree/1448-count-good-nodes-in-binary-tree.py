# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def dfs(root,val):
            if not root:
                return 0
            if root.val>=val:
                self.count+=1
            dfs(root.left,max(root.val,val))
            dfs(root.right,max(root.val,val))
            return self.count
        return dfs(root,root.val)