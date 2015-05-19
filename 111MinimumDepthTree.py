#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        min_level = [0]
        self._minDepth(root, 1, min_level)
        return min_level[0]

    def _minDepth(self, root, level, min_level):
        left = root.left
        right = root.right
        if not left and not right:
            min_level[0] = level
            return
        if left:
            self._minDepth(left, level + 1, min_level)
        if right:
            self._minDepth(right, level + 1, min_level)

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

    def levelOrder(self, root):
        if not root:
            return []
        ret = []
        self._levelOrder(root, 0, ret)
        return ret

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        min_level = [10000000]
        self._minDepth(root, 1, min_level)
        return min_level[0]

    def _minDepth(self, root, level, min_level):
        left = root.left
        right = root.right
        if not left and not right:
            min_level[0] = min(min_level[0], level)
        if left:
            self._minDepth(left, level + 1, min_level)
        if right:
            self._minDepth(right, level + 1, min_level)

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

    def levelOrder(self, root):
        if not root:
            return []
        ret = []
        self._levelOrder(root, 0, ret)
        return ret

t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
#
# t8 = TreeNode(8)

# t7.left = t8

t0.left = t1
# t0.right = t2
# t1.left = t3
# t2.left= t4
# t2.right = t5
# t5.left = t6

# t0.left = t1
# t1.left = t2

solution = Solution()

print solution.minDepth(t0)
print solution.levelOrder(t0)
