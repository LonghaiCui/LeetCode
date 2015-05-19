hash_table = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
class Solution:
    # @param digits, a string
    # @return a string[]
    @staticmethod
    def _letterCombinations(determined, digits, res):
        if digits != '':
            digit = digits[0]
            for char in hash_table[digit]:
                Solution._letterCombinations(determined+char, digits[1:], res)
        else:
            res.append(determined)

    def letterCombinations(self, digits):
        res = []
        Solution._letterCombinations('', digits, res)
        return res

class Solution:
    # @param digits, a string
    # @return a string[]
    @staticmethod
    def _letterCombinations(determined, digits, res):
        if not digits:
            res.append(determined)
            return
        for char in hash_table[digits[0]]:
            Solution._letterCombinations(determined+char, digits[1:], res)

    def letterCombinations(self, digits):
        res = []
        self._letterCombinations('', digits, res)
        return res


class Solution:
    # @param digits, a string
    # @return a string[]
    def _letterCombinations(self,digits):
        if len(digits) == 1:
            ret = []
            for char in hash_table[digits[0]]:
                ret.append(char)
            return ret
        else:
            ret = []
            for char in hash_table[digits[0]]:
                for elt in self._letterCombinations(digits[1:]):
                    ret.append(char+elt)
            return ret

    def letterCombinations(self, digits):
        if not digits:
            return []
        return self._letterCombinations(digits)

solution = Solution()
print solution.letterCombinations('')

# class Solution:
#     # @param num, a list of integer
#     # @return a list of lists of integers
#     def permuteUnique(self, num):
#         if not num:
#             return []
#         num.sort()
#         return self.permute(num)
#
#     def permute(self, num):
#         if len(num) == 1:
#             return [num]
#         ret = []
#         prev = None
#         for i in range(len(num)):
#             if prev != num[i]:
#                 prev = num[i]
#                 for elt in self.permute(num[:i]+num[i+1:]):
#                     ret.append([num[i]]+elt)
#         return ret