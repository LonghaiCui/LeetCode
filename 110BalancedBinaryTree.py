#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    # def __init__(self):
    #     self.level = -1
    #     self.max_level = -1
    #     self.min_level = -1
    #
    # def isBalanced(self, root):
    #     if not root:
    #         return False
    #     stack = [root]
    #     level = 0
    #     while stack:
    #         root = stack.pop(0)
    #         left = root.left
    #         right = root.right
    #         if left:
    #             stack.append(left)
    #         if right:
    #             stack.append(right)
    #         if not left and not right:
    #             if self.level == -1:
    #                 self.level, self.max_level, self.min_level = level, level, level
    #             else:
    #                 self.max_level = max(self.max_level, level)
    #                 self.min_level = min(self.min_level, level)
    #                 if self.max_level - self.min_level == 2:
    #                     return False
    #         else:
    #             level += 1
    #     return True

    def max_level(self, node, max_level, level):

        if not node:
            return

        if max_level[0] < level:
            max_level[0] = level

        left = node.left
        right = node.right

        if left:
            self.max_level(left, max_level, level + 1)
        if right:
            self.max_level(right, max_level, level + 1)


    def isBalanced(self, root):
        if not root:
            return True

        stack = [root]
        while stack:
            node = stack.pop()
            left = node.left
            right = node.right

            left_height = [0]
            right_height = [0]
            if left:
                stack.append(left)
                self.max_level(left, left_height, 1)
            else:
                self.max_level(left, left_height, 0)
            if right:
                stack.append(right)
                self.max_level(right, right_height, 1)
            else:
                self.max_level(right, right_height, 0)


            #print 'left, right', left.val, right.val
            #print 'node.val, left_height[0], right_height[0]', node.val, left_height[0], right_height[0]
            if abs(left_height[0] - right_height[0]) > 1:
                return False

        return True

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
t0.right = t2
t1.left = t3
t2.left= t4
t2.right = t5
t5.left = t6

# t0.left = t1
# t1.left = t2

solution = Solution()
print solution.levelOrder(t0)
print solution.isBalanced(t0)
