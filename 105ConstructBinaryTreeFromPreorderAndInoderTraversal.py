# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Memory Limit
class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        root = TreeNode(preorder[0])
        self._buildTree(preorder, inorder, root)
        return root

    def _buildTree(self, preorder, inorder, root):
        if not preorder:
            return
        for i, num in enumerate(inorder):
            if root.val == num:
                break

        if i != 0:
            root.left = TreeNode(preorder[1])
            self._buildTree(preorder[1:i+1], inorder[:i], root.left)
        if i != len(preorder) - 1:
            root.right = TreeNode(preorder[i+1])
            self._buildTree(preorder[i+1:], inorder[i+1:], root.right)

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

#to use the first solution if possible since we don't have much time
#First accepted solution
class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        return self._buildTree(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def _buildTree(self, preorder, inorder, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return
        root = TreeNode(preorder[pre_start])
        for i in range(in_start, in_end + 1):
            if root.val == inorder[i]:
                break
        if in_start != i:
            root.left = self._buildTree(preorder, inorder, pre_start + 1, pre_start + i - in_start, in_start, i - 1)
        if in_end != i:
            root.right = self._buildTree(preorder, inorder, pre_start + i - in_start + 1, pre_end, i + 1, in_end)
        return root


















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

    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        root = TreeNode(preorder[0])
        self._buildTree(preorder, inorder, root)
        return root

    def _buildTree(self, preorder, inorder, root):
        if not preorder:
            return
        for i, num in enumerate(inorder):
            if root.val == num:
                break
        if i != 0:
            root.left = TreeNode(preorder[1])
            self._buildTree(preorder[1:i+1], inorder[:i], root.left)
        if i != len(preorder) - 1:
            root.right = TreeNode(preorder[i+1])
            self._buildTree(preorder[i+1:], inorder[i+1:], root.right)


    def __init__(self):
        self.preorder = []
        self.index = 0
        self.hash_table = {}

    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        self.preorder = preorder
        self.inorder = inorder

        for i, num in enumerate(inorder):
            self.hash_table[num] = i

        return self._buildTree(0, len(preorder) - 1)

    def _buildTree(self, start, end):
        if self.index > len(self.preorder) - 1:
            return
        self.preorder[self.index] = self.preorder[self.index]
        print 'self.preorder[self.index]', self.preorder[self.index]
        if start > end:
            return

        if start == end:
            node = TreeNode(self.preorder[self.index])
            self.index += 1
            return node

        node = TreeNode(self.preorder[self.index])
        self.index += 1
        # print 'start, end, current', start, end, self.preorder[self.index]
        # print 'index_pre, index_in', self.index, self.hash_table[self.preorder[self.index]]
        print 'self.preorder[self.index]', self.preorder[self.index]
        mid = self.hash_table[self.preorder[self.index-1]]
        node.left = self._buildTree(start, mid - 1)
        node.right = self._buildTree(mid + 1, end)

        return node

solution = Solution()
#ret = solution.buildTree([1,2,3],[2,3,1])
#ret = solution.buildTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
ret = solution.buildTree([1, 2], [2,1])
print solution.levelOrder(ret)
print ret.left
print ret.right

# 
# current_val 1
# current_val 1
# current_val 2
# [[1], [2]]
# <__main__.TreeNode instance at 0x10dbe7a28>
# None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def __init__(self):
        self.preorder = []
        self.preorder_index = 0
        self.inorder_indexes = {}

    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        self.preorder = preorder
        for i, num in enumerate(inorder):
            self.inorder_indexes[num] = i
        return self._buildTree(0, len(preorder) - 1)

    def _buildTree(self, start, end):
        if self.preorder_index == len(self.preorder) or start > end:
            return
        if start == end:
            node = TreeNode(self.preorder[self.preorder_index])
            self.preorder_index += 1
            return node

        mid = self.inorder_indexes[self.preorder[self.preorder_index]]
        node = TreeNode(self.preorder[self.preorder_index])
        self.preorder_index += 1

        node.left = self._buildTree(start, mid - 1)
        node.right = self._buildTree(mid + 1, end)
        return node

#but it took me long time.the help of
