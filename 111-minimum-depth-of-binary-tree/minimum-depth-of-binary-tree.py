# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        # Store pairs of (node, current depth)
        queue = deque([(root, 1)])

        while queue:
            node, d = queue.popleft()
            # If we find a leaf, we can return immediately
            if not node.left and not node.right:
                return d
            # If not a leaf, look at children
            if node.left:
                queue.append((node.left, d + 1))
            if node.right:
                queue.append((node.right, d + 1))
