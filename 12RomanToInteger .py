# __author__ = 'longhaicui'
# class Solution:
#     # @param {string} s
#     # @return {integer}
#     def romanToInt(self, s):
#         numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
#         integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#         visited = {
#             'M':0,
#             'CM':0,
#             'D':0,
#             'CD':0,
#             'C':0,
#             'XC':0,
#             'L':0,
#             'XL':0,
#             'X':0,
#             'IX':0,
#             'V':0,
#             'IV':0,
#             'I':0
#         }
#         res = 0
#         pos = 0
#         if (s[0] not in visited) and (s[0:2] not in visited):
#             return 0
#         if s[0] in visited:
#             cur = s[0]
#         else:
#             cur = s[0:2]
#         print cur
#         for i in range(len(numerals)):
#             if cur not in visited or visited[cur] == 1:
#                 print "hah"
#                 return 0
#             if pos > len(s)-1:
#                 return res
#             visited[cur] = 1
#             if numerals[i] == cur:
#                 res += integers[i]
#                 print res
#                 pos += 1
#                 if numerals[i] in ('I','X','C','M'):
#                     if pos > len(s)-1:
#                         return res
#                     for i in range(2):
#                         res += integers[i]
#                         pos += 1
#                 else:
#                     break
#                 print res
#             elif numerals[i] == s[pos:pos+2]:
#                 cur = numerals[i]
#                 res += integers[i]
#                 pos += 2
#             else:
#                 continue
#         return res


# class Solution:
#     # @param s, a string
#     # @return an integer
#     def romanToInt(self, s):
#         ROMAN_INT = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
#                     'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
#                     'IV': 4, 'I': 1}
#         result = 0
#
#         while s:
#             if s[:2] in ROMAN_INT:
#                 result += ROMAN_INT[s[:2]]
#                 s = s[2:]
#             else:
#                 result += ROMAN_INT[s[:1]]
#                 s = s[1:]
#
#         return result




class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        res = 0
        visited = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }

        while s:

            if s[:2] in visited:
                res += visited[s[:2]]
                s = s[2:]
            else:
                res += visited[s[:1]]
                s = s[1:]
        return res
solution = Solution()
print solution.romanToInt('MMMCMXCIX')
