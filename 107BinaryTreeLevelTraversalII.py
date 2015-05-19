#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def _levelOrder(self, root, level, ret):
        if level > len(ret) - 1:
            ret.append([])
        left = root.left
        right = root.right
        ret[level].append(root.val)
        if left:
            self._levelOrder(left, level + 1, ret)
        if right:
            self._levelOrder(right, level + 1, ret)

    def levelOrderBottom(self, root):
        if not root:
            return []
        ret = []
        self._levelOrder(root, 0, ret)
        new_ret = []
        for i in reversed(range(len(ret))):
            new_ret.append(ret[i])
        return new_ret

t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(1)
t4 = TreeNode(2)
t5 = TreeNode(5)

t0.left = t1
t0.right = t3
t1.left = t2
t3.right = t4

solution = Solution()
print solution.levelOrderBottom(t0)
