#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Preorder
[1, 2, 6, 3, 4, 5]
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return list()
        stack = list()
        ret = list()
        stack.append(root)
        while stack:
            current = stack.pop()
            ret.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return ret


#Preorder
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return list()
        stack = list()
        ret = list()
        current = root
        stack.append(root)
        while stack:
            ret.append(current.val)
            left = current.left
            right = current.right
            if right:
                stack.append(right)
            if left:
                current = left
            else:
                current = stack.pop()
        return ret

#Preorder
[1, 2, 6, 3, 4, 5]
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return list()

        ret = list()
        stack = list()
        stack.append(root)
        visited = {}

        while stack:
            current = stack.pop()

            right = current.right
            left = current.left

            if current in visited:
                ret.append(current.val)
                continue

            if right:
                stack.append(right)

            stack.append(current)
            visited[current] = 1

            if left:
                stack.append(left)

        return ret

    def pre_orderTraversal(self, root):
        if not root:
            return list()

        ret = list()
        stack = list()
        stack.append(root)
        visited = {}

        while stack:
            current = stack.pop()

            right = current.right
            left = current.left

            if current in visited:
                ret.append(current.val)
                continue

            if right:
                stack.append(right)

            if left:
                stack.append(left)

            stack.append(current)
            visited[current] = 1

        return ret

    def post_orderTraversal(self, root):
        if not root:
            return list()

        ret = list()
        stack = list()
        stack.append(root)
        visited = {}

        while stack:
            current = stack.pop()

            right = current.right
            left = current.left

            if current in visited:
                ret.append(current.val)
                continue

            stack.append(current)
            visited[current] = 1

            if right:
                stack.append(right)

            if left:
                stack.append(left)

        return ret

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def __init__(self):
        self.val = -1000000000000

    def isValidBST(self, root):
        if not root:
            return True
        left = root.left
        right = root.right
        if left:
            if not self.isValidBST(left):
                return False
        if self.val < root.val:
            self.val = root.val
        else:
            return False
        if right:
            if not self.isValidBST(right):
                return False
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(1)
t4 = TreeNode(2)
t5 = TreeNode(5)


t1.left = t2
t3.left = t4
# t1.right = t3
# t3.left = t4
# t4.right = t5
#
# t6 = TreeNode(6)
# t2.left = t6

solution = Solution()
print solution.isSameTree(t1, t3)
# print solution.inorderTraversal(t1)
# print solution.pre_orderTraversal(t1)
# print solution.post_orderTraversal(t1)