__author__ = 'longhaicui'
# class Solution:
#     # @param {integer} num
#     # @return {string}
#     def intToRoman(self, num):
#         copy = num
#         M = num / 1000;num -= M * 1000
#         D = num / 500; num -= D * 500
#         C = num / 100; num -= C * 100
#         L = num / 50;  num -= L * 50
#         X = num / 10;  num -= X * 10
#         V = num / 5;   num -= V * 5
#         I = num
#         list = ['I','V','X','L','C','D','M']
#         hash_table = {
#             'M': M,
#             'D': D,
#             'C': C,
#             'L': L,
#             'V': V,
#             'X': X,
#             'I': I
#         }
#         result = ''
#         print hash_table
#         flag = 1
#         for i in range(len(list)):
#             count = hash_table[list[i]]
#             if flag == 0:
#                 flag = 1
#                 continue
#             if count != 4:
#                 result = list[i]*count + result
#             elif hash_table[list[i+1]] == 1:
#                 result = list[i+2] + result
#                 result = list[i] + result
#                 flag = 0
#             else:
#                 result = list[i+1] + result
#                 result = list[i] + result
#
#         return result
#
# solution = Solution()
# print solution.intToRoman(3999)

#Other people's solution
# class Solution:
#     # @return a string
#
#     def intToRoman(self, num):
#         integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#         numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
#         res = ''
#         for i in range(len(integers)):
#             num, remainder = divmod(num, integers[i])
#             res+=num*numerals[i]
#             num = remainder
#
#         return res





# #Using divmod
# class Solution:
#     # @param {integer} num
#     # @return {string}
#     def intToRoman(self, num):
#         M, num = divmod(num, 1000)
#         D, num = divmod(num, 500)
#         C, num = divmod(num, 100)
#         L, num = divmod(num, 50)
#         V, num = divmod(num, 10)
#         X, num = divmod(num, 5)
#         I, num = divmod(num, 1)
#         list = ['I','V','X','L','C','D','M']
#         hash_table = {
#             'M': M,
#             'D': D,
#             'C': C,
#             'L': L,
#             'V': V,
#             'X': X,
#             'I': I
#         }
#         result = ''
#         print hash_table
#         flag = 1
#         for i in range(len(list)):
#             count = hash_table[list[i]]
#             if flag == 0:
#                 flag = 1
#                 continue
#             if count != 4:
#                 result = list[i]*count + result
#             elif hash_table[list[i+1]] == 1:
#                 result = list[i+2] + result
#                 result = list[i] + result
#                 flag = 0
#             else:
#                 result = list[i+1] + result
#                 result = list[i] + result
#
#         return result
#
# solution = Solution()
# print solution.intToRoman(3999)

#169
# class Solution:
#     # @param {integer} num
#     # @return {string}
#     def intToRoman(self, num):
#         M, num = divmod(num, 1000)
#         CM, num = divmod(num, 900)
#         D, num = divmod(num, 500)
#         CD, num = divmod(num,400)
#         C, num = divmod(num, 100)
#         XC, num = divmod(num, 90)
#         L, num = divmod(num, 50)
#         XL, num = divmod(num,40)
#         X, num = divmod(num, 10)
#         IX, num = divmod(num,9)
#         V, num = divmod(num, 5)
#         IV, num = divmod(num,4)
#         I, num = divmod(num, 1)
#         list = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
#         hash_table = {
#             'M': M,
#             'CM': CM,
#             'D': D,
#             'CD': CD,
#             'C': C,
#             'XC': XC,
#             'L': L,
#             'XL': XL,
#             'X': X,
#             'IX': IX,
#             'V': V,
#             'IV':IV,
#             'I': I
#         }
#         result = ''
#         for i in range(len(list)):
#             count = hash_table[list[i]]
#             result += count * list[i]
#         return result
#
# solution = Solution()
# print solution.intToRoman(3999)


class Solution:
    def intToRoman(self, num):
        numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result = ''
        for i in range(len(numerals)):
            count, num = divmod(num, integers[i])
            result += numerals[i] * count
        return result

solution = Solution()
print solution.intToRoman(3999)