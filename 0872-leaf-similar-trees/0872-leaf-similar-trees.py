# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def leaf(root):
            q=[root]
            leaflist=[]
            while q:
                node=q.pop()
                if not node.left and not node.right:
                    leaflist.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            return leaflist

        return leaf(root1)==leaf(root2)
