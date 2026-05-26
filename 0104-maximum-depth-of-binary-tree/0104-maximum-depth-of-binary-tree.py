# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        st=Queue()
        level=0
        st.put(root)
        while not st.empty():
            for i in range(st.qsize()):
                t= st.get()
                if t.left:
                    st.put(t.left)
                if t.right:
                    st.put(t.right)
            level+=1
        return level