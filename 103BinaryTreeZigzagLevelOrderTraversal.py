#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ret = [[]]
        self._zigzagLevelOrder(root, 0, ret)
        return ret

    def _zigzagLevelOrder(self, root, level, ret):
        if len(ret) < level + 1:
            ret.append([])

        left = root.left
        right = root.right

        if level % 2 == 1:
            ret[level].append(root.val)
            print ret[level], id(ret[level]),
        else:
            ret[level] = [root.val] + ret[level]
            print ret[level], id(ret[level])
        if right:
            self._zigzagLevelOrder(right, level + 1, ret)
        if left:
            self._zigzagLevelOrder(left, level + 1, ret)


t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t0.left = t1
t0.right = t3
t1.left = t2
t3.right= t4
# t1.right = t3
# t3.left = t4
# t4.right = t5
#
# t6 = TreeNode(6)
# t2.left = t6

solution = Solution()
print solution.zigzagLevelOrder(t0)
