class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        if s == '':
            return True
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
solution = Solution()
print solution.isValid("]")

# class Solution:
#     # @param s, a string
#     # @return a boolean
#     def isValid(self, s):
#         paren_map = {
#             '(': ')',
#             '{': '}',
#             '[': ']'
#         }
#         stack = []
#
#         for p in s:
#             if p in paren_map:
#                 stack.append(paren_map[p])
#             else:
#                 if not stack or stack.pop() != p:
#                     return False
#
#         return not stack


print 1 if 0 else 3