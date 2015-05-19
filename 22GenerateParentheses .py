# # Definition for singly-linked list.
#
# class Solution:
#     # @param n, an integer
#     # @return a string[]
#     def generateParenthesis(self, n):
#         if n == 0:
#             return
#         if n == 1:
#             return ['()']
#         if n == 2:
#             return ['()()', '(())']
#         res = []
#         determined = ''
#         Solution._generateParenthesis(determined, n, res)
#         return res
#
#     @staticmethod
#     def _generateParenthesis(determined, n, res):
#         if n==0:
#             if determined not in res:
#                 res.append(determined)
#             else:
#                 return
#         else:
#             #Solution._generateParenthesis('()' + determined, n-1, res)
#             #Solution._generateParenthesis('(' + determined + ')', n-1, res)
#             for i in range():
#                 Solution._generateParenthesis(determined)
#             Solution._generateParenthesis(determined + '()', n-1, res)
#             #print n,res
#
# solution = Solution()
# result = solution.generateParenthesis(4)
# print result
# "(((())))" #xx11
#
#
# "((()))()"  #31
# "((())())"  #x21
# "((()()))"  #xx2
#
#
# "(()(()))"  #x12
# "(()()())"  #x111
# "(()())()"
# "(())(())"  #22
#
# "(())()()"  #211
#
#
# "()((()))"  #13
# "()(()())"
# "()(())()"  #121
#
# "()()(())"  #112
# "()()()()"  #4
# test = ["(((())))", #xx11
#
#
# "((()))()",  #31
# "((())())",  #x21
# "((()()))",  #xx2
#
#
# "(()(()))",  #x12
# "(()()())",  #x111
# "(()())()",
# "(())(())",  #22
#
# "(())()()",  #211
#
#
# "()((()))",  #13
# "()(()())",
# "()(())()",  #121
#
# "()()(())",  #112
# "()()()()" ]
# for char in test:
#     if char not in result:
#         print char


# Definition for singly-linked list
class Solution:
    # @param n, an integer
    # @return a string[]
    def generateParenthesis(self, n):
        if n == 1:
            return ['()']
        res = []
        for i in range(n):
            res.append([])
        res[0] = ['()']
        res[1] = ['(())', '()()']
        for i in range(3, n + 1):
            for j in range(1, i):
                for x in res[j-1]:
                    for y in res[i-j-1]:
                        char = x + y
                        if char not in res[i-1]:
                            res[i-1].append(char)
            for char in res[i-2]:
                char = '(' + char + ')'
                res[i-1].append(char)
        return res[n-1]



solution = Solution()
result = solution.generateParenthesis(2)
print result
"(((())))" #xx11


"((()))()"  #31
"((())())"  #x21
"((()()))"  #xx2


"(()(()))"  #x12
"(()()())"  #x111
"(()())()"
"(())(())"  #22

"(())()()"  #211


"()((()))"  #13
"()(()())"
"()(())()"  #121

"()()(())"  #112
"()()()()"  #4
test = ["(((())))", #xx11


"((()))()",  #31
"((())())",  #x21
"((()()))",  #xx2


"(()(()))",  #x12
"(()()())",  #x111
"(()())()",
"(())(())",  #22

"(())()()",  #211


"()((()))",  #13
"()(()())",
"()(())()",  #121

"()()(())",  #112
"()()()()" ]
# temp = (x for x in  [1,2]) + (y for y in [3,4])
# print temp
