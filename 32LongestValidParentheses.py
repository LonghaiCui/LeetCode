#This solution only works when there are more ')'s after '('s
# (()))() working
# (()  not working
#Because start is not moving forward
#The whole idea to mark start position may not work for O(n)
#since start position can only be moved forward when all the elements are scanned!
#Better think of a way to store pos in stack instead of meaningless 1s
#Or extra space list of max_length(OR START position, Exactly START actually) since only scan one using O(n)
# class Stack:
#     def __init__(self):
#         self.max_length = 0
#         self.cur_length = 0
#         self.list = []
#
#     def push(self,data):
#         self.list.append(data)
#         self.cur_length += 1
#         #This is wrong
#         # if len(self.list) > self.max_length:
#         #     self.max_length += 1
#
#     def pop(self):
#         if len(self.list) == 0:
#             return False
#         else:
#             self.list.pop()
#         if len(self.list) == 0:
#             self.max_length += self.cur_length
#             self.cur_length = 0
#
#
# class Solution:
#     # @param {string} s
#     # @return {integer}
#     def longestValidParentheses(self, s):
#         longest = 0
#         length = len(s)
#         for i in range(length):
#             if s[i] == '(':
#                 stack = Stack()
#                 stack.push(1)
#                 for j in range(i+1, length):
#                     if s[j] == ')':
#                         if len(stack.list) == 0:
#                             break
#                         else:
#                             stack.pop()
#                         if len(stack.list) == 0:
#                             longest = max(longest, stack.max_length)
#                     else:
#                         stack.push(1)
#             #Improve for case when longest is bigger than number of left elements
#             if longest >= length - i - 1:
#                 return longest
#
#         return longest







#The list DP is to maintain the start position of longest valid string for current char.
# Change DP when there is elements in the stack, which means start position is somewhere before.
# And if the last DP is changed, set the current DP to the start position of the former start position.
class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        max_len = 0
        start_pos = {}
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                    start_pos[i] = last
                    if start_pos.has_key(last-1):
                        start_pos[i] = start_pos[last - 1]
                    max_len = max(max_len, i - start_pos[i] + 1)
        return max_len
        #print start_pos

solution = Solution()
# print solution.longestValidParentheses('(()))()(())')
# print solution.longestValidParentheses('(()))()')
print solution.longestValidParentheses('()()')
print solution.longestValidParentheses(')')
print solution.longestValidParentheses('((())))()())))(((()()(())))((()(())()((()))())())())()())))))))(((()(())(()))(()()(()()((()))()(())(()(())))))()(())(()()(((()(()()))))((()()))))))()((()())()()))((())()((((()))()()()((()())))())((())))))))(()()((((((()))(((((((()()))((())()(()())()()()(()())(()())(())))()()))))()(((())(())(()())()))()(()))(())((()))))(())))()))((()((()(())(()()()()()))(())())()))))()(()(((())))()()()(((()((()))(()((((((())((()))(()(())(()))(())())))()()))))())(()((()()())()))((((()(()))()()))(()())))((()))(()((((()(())(())()((()))(()))())))(((()(())))((())()(()(((())))())())()()()())((()()))))))(()))(())()(((()))()()((()))(()))(((()))))))))(()(())())(()((())(()()))((())))(()())((((())))(()(()))())(((()(()((()(())((())())(()))(())))()()(())((()()))((()()((()()())())()))())()))())()))())(()(()))(()))()(())))((((())()())()()())((()())(()())(()()))()(())(())))))()()()((()(())(((()(())()()))(()()((()(((()))))))))(((()((()()((()(((((())((()((()((((((((())()))())((())((()((()(()((())(((()(()))())))))))))))))()((()(())())))()(()))(((()))())()(((()))))((()(())(()())(((()(((()((((())()))))(())((()(((((()((()(()()()()((()((((((((((((())()(()))()()(()())()(()(((()((()(()()()())))((())()))())()()))())(((()(())))))()()()(((())))((()(()(((())(())(()((((()(((()(())(((((())()))())())()()(()())((((()(())))((()())))))))))()(()(())))))))()))()())))((())(()()()()()()()(())(()())))))())((()()))))()))))((())((()(((()))))(((()()))()(()((()()())()))(((()(()((())(()(()(()()))()((()(())))()((())))))(())()(())()))((())(((((()))()())(())))((((()((())())(())))(())))))((())())())((((()((())))()()((()()()))()())())(()())(((()))()()))))(()(())(()))()())(()())(()))(((((((()(()))())()())()())((()(((((()())(((())))()())))(()(()(())()((())()))(())))())()))((((()))())((()))(())))))(()))))))(()))))(())))())()()())()()(())()()(((((()))(((()()))()(()((((()(()(()(())))())))())(()()())()(()))())(()()))(()()((()()))))))(())((()()))(())))())())(())((((()))))()))()))()()()))))((((()((())(()))(()()))(())()())(()())))(()(()(())((()())()((())(()))()))()))))((())))(())(()))()()()()()))((())(((()(())))(((((((()(()))(()))())()((()))(()(())((()((()((())))()()((())))))((((())()())(()()(((()()((()))()()((())))(((()())((((()(())())))())()()()(())()))))))()()((()))())(()(((()()))((())))())())())((((()(((()(())())()())((()((()(()((())()(()))()((())))()(()))))(((()))())())(()((()))))()()(((((()))())))(()(()(())((((())())))((()()())(((((((()(()(()))(())))))()))(()(((((())()))((()()()()((()))()(()()()()))(()))))())())()))()(()()(((())((()))(()())))((()()(((())())))))))(())))((()(()(((())((((()))))(()()()))))(((((((())(()(()))(()(())((())(()(()(()(()())(())()(())(()()(()(()))())(())()()(((()())(())(()(((()()(())()((((()()))())(((()(((((()())()(())))()))))(()(()()(()(()()(((()))()))((()())))()(()(())))))))())((((()()))(()))))()((()))(()))())()))()))))(()(())()()()))(((((()))()())())(()())())))()())))))()()()())))))(())(((()))((())((()()))))()((((()(()(()))))(()(())(((())(()()(((()(())()())(()()(()(()())))()())))(((()()((()())()()((()))()))(((()((((()(((()(((()(()())((()))))()(()())(())()(()(((())((()))(())()(())()(()(())()))())()))()())(()))))()))))((()()()((()(()()(())))())(())()(()()))))))))()((()))((((())))())))((()()()(()(()((((()((()))()()((())((())(()))))(())())(((()()(()))))))(()()))()))((()(()(())()))(((())()))(())(()((((()((()()()))()()))(()()(())())((((((())(())((()())()(()())))()))())(()()(()(()()()(()()()()))(()(()()())())((()()()(((()((()())()()((()()(()((()())()())()((()))(()((()())))))))(())((((())(((((())(((())(()))(((()((()()())()((()(()))()()()(()((((())))(())())))((())))(()(((((()()()((())((((((((()()((((())))())())())))))))(((()())(((()))())))()))((())())())))))))))(()()(((())))))(())()()))((())()))(()(()))((()(()((((()(()(((()))))()))(()(()))())())()()(((())())(((()))))(((()())))()(()())()())()))())())(()()(((()()))(())(((()((())((((())))))((()))))(()((()(())))()(())((()(())((()(()())())))()))))(())())(()())()()()((())))((()()))()()()((((()())))))()))))()))())()((()(())()()(())(((()((()))(()(()()))(()))()))))))))))))(()()))(((())((()(((()()()(()())((((()(()()()))())))())(()())))(()((((()))((()()())(((()))()())(()(()((()(()))))(())()()((()())((()(()(()))((()((()())(((()(((((()()()))(()()(()(((()(()())()()()))((()(()())))())(()(()))(())()())))()()()))()())(()(((((()))()()((((()()()()))()()(()((()))(()))))))))))()))()(()((((((())(()))()((())))(((((())))))(()))))()()(()()()(((((()))()())()((((()()))()(())())))(((()((())))))))))(()()()((()))(()())((())))()()((()())))()()(()))))))))()(((()(()))()())((((((())))(((()(()())())))(())())())()()((((()(()(((())(()()(((((()))(()(())()))))))()))()())))()()(()))(((()))()())))((())(((()()))((((((())))(((())()()(()((()))())(()((()()(((())())()))()()())())(()()((((((((())))()(((())(()))))()()())()(())))(((((()())(((())()()))))()((())())(())()(()(()()((()))()(()(((()))))()()())(())()()()(((()((()()()(()())())(())()(((((()())(())()((((()()()))()((())()((()(()(((()(()))()())())()())()(()()(()(((()))()(())(()())(())((())()((()()())(()))))()(()()))))((())()()((()((()()(()((()()())(())))))())))()))))(((((()(()())(()))((()))()(()())())())))()(()()(()((())))))()()))((())((((()))))())((()))())((())((()(()((()))()()()))()((((((())((((((()((((((((()))(()(((()(((((((((())(())())()())))))))())())))()))(()))))()(()))(())))()()()((()()))(())(()))(()()(()())))()(()()()()())))(())((((()))(((((())(()(((((())((()((((()))(((((()))(()())()))))())()))()(()()))((((()))()())(())))()((())))(((((()()((()()((()))))()((())())()))(((((((((()((())((((())()())))(())())()))())))())()))()(()()(()))(()()()((())((()))())))()(()())()(((((((()))))(()()()((()(())))())()))((())())(()(()(())()()())))))(()()()))())()))()())(((())(())))()(())())))()((()(()(())()()()((()))()))((())((((()((((((()()()))()))())())))))()(())(()())))()(((()())(((())))((())()()))((())())()()(()()())()))())(((()((()(((()())(()(())(((())))()))))))())()((((((()))))))()(()))()))())))())((((())(())()(())()))()))((((((((()()(())())((((())))((((()(())()()(())()))())()))(((()((()))()(((((()()()))))(()(()())))(((()(((()(())())((((())(()((()((()(()()(()()))()))()()))()))))))())()(())())))(((())))((()))((()(())())((())))((()))()))(((()))))(()())()())())()())))())))(())))(())())()((()())()()))((()()())(((((()())))())))()()()((((((())())()((())()))(()))()(()())()())(())()())((()((())(())()()()()((())(()())()()((())))()(((()(()(((((()(())))()(()))()(()))()))())()))()())()(()))))()()())(((())((()((())(()(()))()((()))))))(())(()(())())()()((())((())((((())))))(()()())(()()())(())())(((()()(())(())))()()))(())))))())(())()(((())())))((()(((())))(()((())()))()))((()()())()(((((())((((())))(())()()((()()(()()))(()((()))((())())))))))()())))())())((()(()()()()()))))()))((())(((((()())(()))((())))((()(())))))))))(((())(()(())(()(())((()((()))()((())())()())()((()(())())()(((()()((()(()())))))())((())(((()())(((()(()((())((()(((())(()()((((((()))())))())(()(()(()()())())((()))((())(())(())())))()(()())()))())(())((((())()((())))))(()()((())(((((()))()()))()()())(()(((()))())()()()))(((()()))(()(()((())(())))()()((((()()))()(())()())()()()()()(()()))(((())(((()()()((((((((((()()()(((()))))))())))()(((((((()((((((((()))()(((())())())())((((((()()))(()))()))))(())()())))())(()))(((())()()()((()()((())(()))((()(()())))()(()((()((())()()()()(())()()((())())())()()))()()))))((()()((())(((())(())())))((())())())(()))))())))))()((()(()(()))))()))((((())((())())(()))))()((()))(())((()()))()()((())(())())))(())))))()()(()())((()(())(((()((())))()())))()))()))))(())()(()))((()()()()))(())))(()()(())(((()(((()()))()((()))())()))(()(()))())))))))()((()(()))(((())())(())(()))(())(()((()))))))(()())(()()()(((()(((((()))((()))))(()))(())())(((()(()())(()()()()))())(()((()(()))()))())))(((()(()))))()))(()()((())())(()()())((()))(())))()()))(())))())))(()((())((()))((()))))())()()()((((((())((())()))(()))(())(())())))()())()((())))((()()())(()))(((()))())())))(())(())())()())()))((((()()()()))(())))((((())))(())(()((((()))())()))))))()()()))())))()((())))))((())())))()()(()()(()(()()()())((((())))(())(((())(()(()((((())(()()()(()(()((())(())(()())((((()((()((((((()((((())(((()())()((((()((())()(()(()(()((()()()(()(()())(((()(())(()(())(())(()))()((((((((()()(())))(()()(((())()(()(((((()())((()(())()())(((()(()(())()((((((((())()((()()((((())(((()(()((()((((()((((()(()(())())()(((()()))))))(()(((())()(((()())))((()))))(()()))))(()))))))((())())((())))()()()(()((()))()))()))()()()()()))(((((((()((()))((())()(()(()))()((((((((((((()(())))))(()())))()(()()(()(()()))))(((((()()((())()))())()()()))(())())()())()()((()()(()(()()(()))))))()()))(()()((()))))()((()()()())))(((()(((()()(())(())(()(((())(()((()(()))(()()((())()(()()())()))))))(()()((())((()())))(())(()))()(()))(()))()))()(())()(()())))(()))(()()(((()))))())))))((())())))))()()()))(()))((()())())()()))(((())((()((())()(()))()((()))()(())))))))()()())())))(()()(())(()))(())))))()(()))(()()))))))))((((()()()()()))(()))((()((())))(()())(((()()()(())))))()))()())())(()()()))))))((()())))((())))(())()((()))()(()())())))))(((()()(()(())()())(((((()))((()(())(())))))))()()))))))((()((((()()))()))(()()))(()()(())))))(((()()))(()())))(())()((()((()(((()()()()((()())())(()(((((((()((((())(()((((()()(())))))(()())))))(()())))())(())))((()(()))(()())(((())))((((())))))((()))()(((((((())())())((())))))))(()))))))))()((()()())((())))(())))((()(((()(())(())))()()()()))(())(()(())()())(())))()())((()((()((()()((())())))(()((())()()))()))((()()(()))(((((((()))((())((())((())()()((((((((()())()()()))(()()(((()(())()))()))()))()()(()(((((()))))((())(((()))()((((((((()()()()(()))()(()))()(())))))))()((((()()((()(())()((()))((()()(()()))))))))))(())(()))()()((((())))()((())(()((()((()(())()))()()((((()))))()))())))))())(((()()))()))()(()))(()))()((()((((((())())))()))()((())(()(())))))))()))(()()()())())()))((()))(()((()((()())))))((((())()()())(())())()((()((()())()())()(()))))((()())))()))()()))))()((())))())(()))()))(()((())(()))))()()))(()()((((()()))(((()()())(()(()(((()))())))((((()())()()()(())()()()((()))))((()()(()()))()())))(((((()(())())))))(()))))())))(())())()))))((()))))))(((())(((())()(((())))(()))()())(((()(()(((()))))()(()()(())())))))())())()()((())))()(())((()))((())(()())(()()()(()()())((())())))))((()(()())()()))))(()()(()()()(()()))((((((()))(()())(())(())())((())(()(()))((()()(()))))()))()(())))())))())(()((())))((())(()()()(()))((()((((((()())()()))))()))((()((())()))()((((()()()(((())())))()()()())())())(()())()))()(())(())()))())((()(((((()))(())(((((()))(()())(()(()(())()((()(()(()))()(()))))()(((())(()((((((()))(()(((()()())()())((()())))((()((()())()((((((())()))(()))))(()()()()))())())((((((((())((((()()()))(())()()))(()(()()(()(()))))(()))(()()()(())()()(())(()))())((()()((()(()))()))))())((()())())(((((()(()()))((()()()))()()(()(()(((()())(((((((((()))()())(()(()(())(((((()()))))(()())(()())())(())))))((()))())(((()((((()))()))(()(()(((()()(()(((()()))(())))((((()(()()))))((((()()())()))())()))))((())((((((())()()))()))()(((()((())(()((((()())())((((((((((()(((((()())()()(()))))))()((((())())(((()()((((()()())()(((((())))()))(())())(((()(((())()))()()()()(())))(()(((()(()))())))()(((()()()()()(()(((()(((()))()(())(())()()))()((()))))))()(((((()(()()((())(())((())))()(()())(())))())((())(()(()()(((())((()()(()()((()))))())))()(()))()))))))())())))((((((()())))(())(()))()()))()(())))))))((()))(()()()()))()())()()()()))()()())))))))((())(())))(()))(())((()())))(()(((()))((((())())))(())((())())))))(((()())(())()(())))((()()()((()(()))()))(())))((()(()()((()()()))((()))((()))()))(()())()()(((((((((()(()))()())()((())((((((((()(())()(((()((())()((((((((()))())))(()((()((())())())((()()())))(()(()((((((()))))((((())))((()()(())()())()()())(())(((()(()()(())(((())((((())()()(()()(((())()(())((()(()(((()(()())))()))((()()())(())))))(()(()))()))()(()))))(()((()))()())(())(())(()))((()())()))())()())((((()))))())())(((()))(((()()((()((())(())()()))))(((()((((()(((((((((())()()()(())((()(()()(()()(()()(())()())(((((()))))()(())(((()((((()())(()(((()))))()))())((((()()((()(()))))((())(())(()(()))()()(((()))(((((((((()())))((())()(()(((((((()))))))()()(())(((()(()())()()))((()()))((((()(())())))((()())))))()))))))))()()(((())())((()))())((())((()()))())((((((((())((()((())())))))()()))))))()()(())))))()))()()(((()))))(())((((()()()()))((()((((()()(())(((((()())()))))))())())()((((((((((()))()))((()))(())())(()(()(())((()()(()((())(())((((())(()()(()((()((()(((((()(()()((((())(())())(()()())()())((()(())()(())()))))')
#s = '((())))()())))(((()()(())))((()(())()((()))())())())()())))))))(((()(())(()))(()()(()()((()))()(())(()(())))))()(())(()()(((()(()()))))((()()))))))()((()())()()))((())()((((()))()()()((()())))())((())))))))(()()((((((()))(((((((()()))((())()(()())()()()(()())(()())(())))()()))))()(((())(())(()())()))()(()))(())((()))))(())))()))((()((()(())(()()()()()))(())())()))))()(()(((())))()()()(((()((()))(()((((((())((()))(()(())(()))(())())))()()))))())(()((()()())()))((((()(()))()()))(()())))((()))(()((((()(())(())()((()))(()))())))(((()(())))((())()(()(((())))())())()()()())((()()))))))(()))(())()(((()))()()((()))(()))(((()))))))))(()(())())(()((())(()()))((())))(()())((((())))(()(()))())(((()(()((()(())((())())(()))(())))()()(())((()()))((()()((()()())())()))())()))())()))())(()(()))(()))()(())))((((())()())()()())((()())(()())(()()))()(())(())))))()()()((()(())(((()(())()()))(()()((()(((()))))))))(((()((()()((()(((((())((()((()((((((((())()))())((())((()((()(()((())(((()(()))())))))))))))))()((()(())())))()(()))(((()))())()(((()))))((()(())(()())(((()(((()((((())()))))(())((()(((((()((()(()()()()((()((((((((((((())()(()))()()(()())()(()(((()((()(()()()())))((())()))())()()))())(((()(())))))()()()(((())))((()(()(((())(())(()((((()(((()(())(((((())()))())())()()(()())((((()(())))((()())))))))))()(()(())))))))()))()())))((())(()()()()()()()(())(()())))))())((()()))))()))))((())((()(((()))))(((()()))()(()((()()())()))(((()(()((())(()(()(()()))()((()(())))()((())))))(())()(())()))((())(((((()))()())(())))((((()((())())(())))(())))))((())())())((((()((())))()()((()()()))()())())(()())(((()))()()))))(()(())(()))()())(()())(()))(((((((()(()))())()())()())((()(((((()())(((())))()())))(()(()(())()((())()))(())))())()))((((()))())((()))(())))))(()))))))(()))))(())))())()()())()()(())()()(((((()))(((()()))()(()((((()(()(()(())))())))())(()()())()(()))())(()()))(()()((()()))))))(())((()()))(())))())())(())((((()))))()))()))()()()))))((((()((())(()))(()()))(())()())(()())))(()(()(())((()())()((())(()))()))()))))((())))(())(()))()()()()()))((())(((()(())))(((((((()(()))(()))())()((()))(()(())((()((()((())))()()((())))))((((())()())(()()(((()()((()))()()((())))(((()())((((()(())())))())()()()(())()))))))()()((()))())(()(((()()))((())))())())())((((()(((()(())())()())((()((()(()((())()(()))()((())))()(()))))(((()))())())(()((()))))()()(((((()))())))(()(()(())((((())())))((()()())(((((((()(()(()))(())))))()))(()(((((())()))((()()()()((()))()(()()()()))(()))))())())()))()(()()(((())((()))(()())))((()()(((())())))))))(())))((()(()(((())((((()))))(()()()))))(((((((())(()(()))(()(())((())(()(()(()(()())(())()(())(()()(()(()))())(())()()(((()())(())(()(((()()(())()((((()()))())(((()(((((()())()(())))()))))(()(()()(()(()()(((()))()))((()())))()(()(())))))))())((((()()))(()))))()((()))(()))())()))()))))(()(())()()()))(((((()))()())())(()())())))()())))))()()()())))))(())(((()))((())((()()))))()((((()(()(()))))(()(())(((())(()()(((()(())()())(()()(()(()())))()())))(((()()((()())()()((()))()))(((()((((()(((()(((()(()())((()))))()(()())(())()(()(((())((()))(())()(())()(()(())()))())()))()())(()))))()))))((()()()((()(()()(())))())(())()(()()))))))))()((()))((((())))())))((()()()(()(()((((()((()))()()((())((())(()))))(())())(((()()(()))))))(()()))()))((()(()(())()))(((())()))(())(()((((()((()()()))()()))(()()(())())((((((())(())((()())()(()())))()))())(()()(()(()()()(()()()()))(()(()()())())((()()()(((()((()())()()((()()(()((()())()())()((()))(()((()())))))))(())((((())(((((())(((())(()))(((()((()()())()((()(()))()()()(()((((())))(())())))((())))(()(((((()()()((())((((((((()()((((())))())())())))))))(((()())(((()))())))()))((())())())))))))))(()()(((())))))(())()()))((())()))(()(()))((()(()((((()(()(((()))))()))(()(()))())())()()(((())())(((()))))(((()())))()(()())()())()))())())(()()(((()()))(())(((()((())((((())))))((()))))(()((()(())))()(())((()(())((()(()())())))()))))(())())(()())()()()((())))((()()))()()()((((()())))))()))))()))())()((()(())()()(())(((()((()))(()(()()))(()))()))))))))))))(()()))(((())((()(((()()()(()())((((()(()()()))())))())(()())))(()((((()))((()()())(((()))()())(()(()((()(()))))(())()()((()())((()(()(()))((()((()())(((()(((((()()()))(()()(()(((()(()())()()()))((()(()())))())(()(()))(())()())))()()()))()())(()(((((()))()()((((()()()()))()()(()((()))(()))))))))))()))()(()((((((())(()))()((())))(((((())))))(()))))()()(()()()(((((()))()())()((((()()))()(())())))(((()((())))))))))(()()()((()))(()())((())))()()((()())))()()(()))))))))()(((()(()))()())((((((())))(((()(()())())))(())())())()()((((()(()(((())(()()(((((()))(()(())()))))))()))()())))()()(()))(((()))()())))((())(((()()))((((((())))(((())()()(()((()))())(()((()()(((())())()))()()())())(()()((((((((())))()(((())(()))))()()())()(())))(((((()())(((())()()))))()((())())(())()(()(()()((()))()(()(((()))))()()())(())()()()(((()((()()()(()())())(())()(((((()())(())()((((()()()))()((())()((()(()(((()(()))()())())()())()(()()(()(((()))()(())(()())(())((())()((()()())(()))))()(()()))))((())()()((()((()()(()((()()())(())))))())))()))))(((((()(()())(()))((()))()(()())())())))()(()()(()((())))))()()))((())((((()))))())((()))())((())((()(()((()))()()()))()((((((())((((((()((((((((()))(()(((()(((((((((())(())())()())))))))())())))()))(()))))()(()))(())))()()()((()()))(())(()))(()()(()())))()(()()()()())))(())((((()))(((((())(()(((((())((()((((()))(((((()))(()())()))))())()))()(()()))((((()))()())(())))()((())))(((((()()((()()((()))))()((())())()))(((((((((()((())((((())()())))(())())()))())))())()))()(()()(()))(()()()((())((()))())))()(()())()(((((((()))))(()()()((()(())))())()))((())())(()(()(())()()())))))(()()()))())()))()())(((())(())))()(())())))()((()(()(())()()()((()))()))((())((((()((((((()()()))()))())())))))()(())(()())))()(((()())(((())))((())()()))((())())()()(()()())()))())(((()((()(((()())(()(())(((())))()))))))())()((((((()))))))()(()))()))())))())((((())(())()(())()))()))((((((((()()(())())((((())))((((()(())()()(())()))())()))(((()((()))()(((((()()()))))(()(()())))(((()(((()(())())((((())(()((()((()(()()(()()))()))()()))()))))))())()(())())))(((())))((()))((()(())())((())))((()))()))(((()))))(()())()())())()())))())))(())))(())())()((()())()()))((()()())(((((()())))())))()()()((((((())())()((())()))(()))()(()())()())(())()())((()((())(())()()()()((())(()())()()((())))()(((()(()(((((()(())))()(()))()(()))()))())()))()())()(()))))()()())(((())((()((())(()(()))()((()))))))(())(()(())())()()((())((())((((())))))(()()())(()()())(())())(((()()(())(())))()()))(())))))())(())()(((())())))((()(((())))(()((())()))()))((()()())()(((((())((((())))(())()()((()()(()()))(()((()))((())())))))))()())))())())((()(()()()()()))))()))((())(((((()())(()))((())))((()(())))))))))(((())(()(())(()(())((()((()))()((())())()())()((()(())())()(((()()((()(()())))))())((())(((()())(((()(()((())((()(((())(()()((((((()))())))())(()(()(()()())())((()))((())(())(())())))()(()())()))())(())((((())()((())))))(()()((())(((((()))()()))()()())(()(((()))())()()()))(((()()))(()(()((())(())))()()((((()()))()(())()())()()()()()(()()))(((())(((()()()((((((((((()()()(((()))))))())))()(((((((()((((((((()))()(((())())())())((((((()()))(()))()))))(())()())))())(()))(((())()()()((()()((())(()))((()(()())))()(()((()((())()()()()(())()()((())())())()()))()()))))((()()((())(((())(())())))((())())())(()))))())))))()((()(()(()))))()))((((())((())())(()))))()((()))(())((()()))()()((())(())())))(())))))()()(()())((()(())(((()((())))()())))()))()))))(())()(()))((()()()()))(())))(()()(())(((()(((()()))()((()))())()))(()(()))())))))))()((()(()))(((())())(())(()))(())(()((()))))))(()())(()()()(((()(((((()))((()))))(()))(())())(((()(()())(()()()()))())(()((()(()))()))())))(((()(()))))()))(()()((())())(()()())((()))(())))()()))(())))())))(()((())((()))((()))))())()()()((((((())((())()))(()))(())(())())))()())()((())))((()()())(()))(((()))())())))(())(())())()())()))((((()()()()))(())))((((())))(())(()((((()))())()))))))()()()))())))()((())))))((())())))()()(()()(()(()()()())((((())))(())(((())(()(()((((())(()()()(()(()((())(())(()())((((()((()((((((()((((())(((()())()((((()((())()(()(()(()((()()()(()(()())(((()(())(()(())(())(()))()((((((((()()(())))(()()(((())()(()(((((()())((()(())()())(((()(()(())()((((((((())()((()()((((())(((()(()((()((((()((((()(()(())())()(((()()))))))(()(((())()(((()())))((()))))(()()))))(()))))))((())())((())))()()()(()((()))()))()))()()()()()))(((((((()((()))((())()(()(()))()((((((((((((()(())))))(()())))()(()()(()(()()))))(((((()()((())()))())()()()))(())())()())()()((()()(()(()()(()))))))()()))(()()((()))))()((()()()())))(((()(((()()(())(())(()(((())(()((()(()))(()()((())()(()()())()))))))(()()((())((()())))(())(()))()(()))(()))()))()(())()(()())))(()))(()()(((()))))())))))((())())))))()()()))(()))((()())())()()))(((())((()((())()(()))()((()))()(())))))))()()())())))(()()(())(()))(())))))()(()))(()()))))))))((((()()()()()))(()))((()((())))(()())(((()()()(())))))()))()())())(()()()))))))((()())))((())))(())()((()))()(()())())))))(((()()(()(())()())(((((()))((()(())(())))))))()()))))))((()((((()()))()))(()()))(()()(())))))(((()()))(()())))(())()((()((()(((()()()()((()())())(()(((((((()((((())(()((((()()(())))))(()())))))(()())))())(())))((()(()))(()())(((())))((((())))))((()))()(((((((())())())((())))))))(()))))))))()((()()())((())))(())))((()(((()(())(())))()()()()))(())(()(())()())(())))()())((()((()((()()((())())))(()((())()()))()))((()()(()))(((((((()))((())((())((())()()((((((((()())()()()))(()()(((()(())()))()))()))()()(()(((((()))))((())(((()))()((((((((()()()()(()))()(()))()(())))))))()((((()()((()(())()((()))((()()(()()))))))))))(())(()))()()((((())))()((())(()((()((()(())()))()()((((()))))()))())))))())(((()()))()))()(()))(()))()((()((((((())())))()))()((())(()(())))))))()))(()()()())())()))((()))(()((()((()())))))((((())()()())(())())()((()((()())()())()(()))))((()())))()))()()))))()((())))())(()))()))(()((())(()))))()()))(()()((((()()))(((()()())(()(()(((()))())))((((()())()()()(())()()()((()))))((()()(()()))()())))(((((()(())())))))(()))))())))(())())()))))((()))))))(((())(((())()(((())))(()))()())(((()(()(((()))))()(()()(())())))))())())()()((())))()(())((()))((())(()())(()()()(()()())((())())))))((()(()())()()))))(()()(()()()(()()))((((((()))(()())(())(())())((())(()(()))((()()(()))))()))()(())))())))())(()((())))((())(()()()(()))((()((((((()())()()))))()))((()((())()))()((((()()()(((())())))()()()())())())(()())()))()(())(())()))())((()(((((()))(())(((((()))(()())(()(()(())()((()(()(()))()(()))))()(((())(()((((((()))(()(((()()())()())((()())))((()((()())()((((((())()))(()))))(()()()()))())())((((((((())((((()()()))(())()()))(()(()()(()(()))))(()))(()()()(())()()(())(()))())((()()((()(()))()))))())((()())())(((((()(()()))((()()()))()()(()(()(((()())(((((((((()))()())(()(()(())(((((()()))))(()())(()())())(())))))((()))())(((()((((()))()))(()(()(((()()(()(((()()))(())))((((()(()()))))((((()()())()))())()))))((())((((((())()()))()))()(((()((())(()((((()())())((((((((((()(((((()())()()(()))))))()((((())())(((()()((((()()())()(((((())))()))(())())(((()(((())()))()()()()(())))(()(((()(()))())))()(((()()()()()(()(((()(((()))()(())(())()()))()((()))))))()(((((()(()()((())(())((())))()(()())(())))())((())(()(()()(((())((()()(()()((()))))())))()(()))()))))))())())))((((((()())))(())(()))()()))()(())))))))((()))(()()()()))()())()()()()))()()())))))))((())(())))(()))(())((()())))(()(((()))((((())())))(())((())())))))(((()())(())()(())))((()()()((()(()))()))(())))((()(()()((()()()))((()))((()))()))(()())()()(((((((((()(()))()())()((())((((((((()(())()(((()((())()((((((((()))())))(()((()((())())())((()()())))(()(()((((((()))))((((())))((()()(())()())()()())(())(((()(()()(())(((())((((())()()(()()(((())()(())((()(()(((()(()())))()))((()()())(())))))(()(()))()))()(()))))(()((()))()())(())(())(()))((()())()))())()())((((()))))())())(((()))(((()()((()((())(())()()))))(((()((((()(((((((((())()()()(())((()(()()(()()(()()(())()())(((((()))))()(())(((()((((()())(()(((()))))()))())((((()()((()(()))))((())(())(()(()))()()(((()))(((((((((()())))((())()(()(((((((()))))))()()(())(((()(()())()()))((()()))((((()(())())))((()())))))()))))))))()()(((())())((()))())((())((()()))())((((((((())((()((())())))))()()))))))()()(())))))()))()()(((()))))(())((((()()()()))((()((((()()(())(((((()())()))))))())())()((((((((((()))()))((()))(())())(()(()(())((()()(()((())(())((((())(()()(()((()((()(((((()(()()((((())(())())(()()())()())((()(())()(())()))))'
#print len(s)
# start_pos = [None for x in range(3)]
# print start_pos

#Two stack
class Solution:
# @param s, a string
# @return an integer
    def longestValidParentheses(self, s):
        stack,index_stack = [],[-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                index_stack.append(i)
            else:
                if stack != []:
                    stack.pop()
                    index_stack.pop()
                else:
                    index_stack.append(i)
        if len(index_stack) == 1:
            max_len = len(s)
        else:
            index_stack.append(len(s))
            for i in range(len(index_stack)-1):
                if index_stack[i+1] - index_stack[i] != 1:
                    if max_len < index_stack[i+1] - index_stack[i] - 1:
                        max_len = index_stack[i+1] - index_stack[i] - 1
        return max_len