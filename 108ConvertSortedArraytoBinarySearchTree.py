#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) / 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

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


solution = Solution()
ret = solution.sortedArrayToBST([1,2,3,4,5,6,7])
print solution.levelOrder(ret)

# print solution.pre_orderTraversal(t1)
# print solution.post_orderTraversal(t1)