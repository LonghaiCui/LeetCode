# class Solution:
#     # @param {integer} n
#     # @return {string}
#     def countAndSay(self, n):
#         if n == 1:
#             return '1'
#         if n == 2:
#             return '11'
#         if n == 3:
#             return '21'
#         if n == 4:
#             return '1211'
#         cur_string = '1211'
#         while n > 5:
#             cur_char = cur_string[0]
#             cur_string = cur_string[1:]
#             cur_num = 1
#             new_string = ''
#             while cur_string:
#                 if cur_char == cur_string[0]:
#                     cur_num += 1
#                 else:
#                     #Wrong order
#                     # cur_num = 1
#                     # new_string += (str(cur_num) + cur_char)
#                     # cur_char = cur_string[0]
#                     new_string += (str(cur_num) + cur_char)
#                     cur_char = cur_string[0]
#                     cur_num = 1
#                 cur_string = cur_string[1:]
#             new_string += (str(cur_num) + cur_char)
#             cur_string = new_string
#             n -= 1
#         return new_string


def _countAndSay(n, determined):
    if n == 4:
        return determined
    else:
        cur_char = determined[0]
        cur_num = 1
        new_string = ''
        for i in range(1,len(determined)):
            if cur_char == determined[i]:
                cur_num += 1
            else:
                new_string = new_string + str(cur_num) + cur_char
                cur_char = determined[i]
                cur_num = 1
        new_string = new_string + str(cur_num) + cur_char
        return _countAndSay(n-1, new_string)

#Recursion
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        if n == 3:
            return '21'
        if n == 4:
            return '1211'
        return _countAndSay(n,'1211')
solution = Solution()
print solution.countAndSay(7)

