# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#First accept
class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder:
            return
        inorder_indexes = {}
        for i, num in enumerate(inorder):
            inorder_indexes[num] = i
        return self._buildTree(0, len(inorder)-1, [len(inorder)-1], inorder_indexes, inorder, postorder)

    def _buildTree(self, start, end, index, inorder_indexes, inorder, postorder):
        if index[0] == -1 or start > end:
            return

        node_val = postorder[index[0]]
        node = TreeNode(node_val)
        #print node_val

        index[0] -= 1
        if start == end:
            return node

        mid = inorder_indexes[node_val]
        #print 'mid', mid
        node.right = self._buildTree(mid+1, end, index, inorder_indexes, inorder, postorder)
        node.left = self._buildTree(start, mid-1, index, inorder_indexes, inorder, postorder)

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

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def __init__(self):
        self.index = 0
        self.inorder_indexes = {}
        self.postorder = []

    def buildTree(self, inorder, postorder):
        if not inorder:
            return
        self.postorder = postorder
        self.index = len(inorder)-1
        for i, num in enumerate(inorder):
            self.inorder_indexes[num] = i
        return self._buildTree(0, len(inorder)-1)

    def _buildTree(self, start, end):
        if self.index == -1 or start > end:
            return

        node_val = self.postorder[self.index]
        node = TreeNode(node_val)
        self.index -= 1
        if start == end:
            return node

        mid = self.inorder_indexes[node_val]

        node.right = self._buildTree(mid+1, end)
        node.left = self._buildTree(start, mid-1)

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
#ret = solution.buildTree([1,2,3],[2,3,1])
ret = solution.buildTree([4,2,5,1,3,6],[4,5,2,6,3,1])
#ret = solution.buildTree([1, 2], [2, 1])
print solution.levelOrder(ret)



