__author__ = 'longhaicui'

#Original
# class Solution:
#     # @param {integer} x
#     # @return {integer}
#     def reverse(self, x):
#         if x == 0:
#             return 0
#         new = []
#         negative = 1
#         if x < 0:
#             x = 0 - x
#             negative = -1
#         while x > 0:
#             y = x%10
#             x = x/10
#             new.append(str(y))
#         result = int(''.join(new))
#         if result > pow(2,31):
#             return 0
#         else:
#             return result * negative

#int
# class Solution:
#     # @param {integer} x
#     # @return {integer}
#     def reverse(self, x):
#         if x == 0:
#             return 0
#         flag = 1
#         result = 0
#         if x < 0:
#             y = -x
#             flag = -1
#         else:
#             y = x
#
#         while (y>0):
#             result = result * 10 + (y % 10)
#             y /= 10
#
#         if result > pow(2,31):
#             return 0
#         else:
#             return result * flag

#int->str->int
#int->str->int
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x == 0:
            return 0
        flag = 1
        if x < 0:
            flag = -1
            result = int(str(x)[1:][::-1])
        else:
            result = int(str(x)[::-1])
        # Not      x > pow(2,31):
        if result > pow(2,31):
            return 0
        else:
            return flag * result
solution = Solution()
print solution.reverse(123)



