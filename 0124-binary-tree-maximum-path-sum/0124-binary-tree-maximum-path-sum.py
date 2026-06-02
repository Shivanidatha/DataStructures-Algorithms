# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res= root.val

        def traverse(node):
            if not node:
                return 0
            leftmax= traverse(node.left)
            rightmax=traverse(node.right)
            leftmax=max(leftmax,0)
            rightmax=max(rightmax,0)
            nonlocal res
            res= max(res, node.val+leftmax+rightmax)
            return node.val+max(leftmax,rightmax)
        traverse(root)
        return res