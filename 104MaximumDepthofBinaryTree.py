# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def _maxDepth(self, root, dep, max_dep):
        if max_dep[0] < dep:
            max_dep[0] = dep
        left = root.left
        right = root.right
        if left:
            self._maxDepth(left, dep + 1, max_dep)
        if right:
            self._maxDepth(right, dep + 1, max_dep)

    def maxDepth(self, root):
        if not root:
            return 0
        max_dep = [1]
        self._maxDepth(root, 1, max_dep)
        return max_dep[0]
