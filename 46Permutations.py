#Init self.res = []
#Append to res list when satisfies
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.hash_table = {}

    def _permute(self,num,determined):
        if not num :#and (determined not in self.res):
            self.res.append(determined)
        for i in range(len(num)):
            new_list = list(determined)
            new_list.append(num[i])
            if str(new_list) not in self.hash_table:
                self.hash_table[str(new_list)] = 1
                self._permute(num[:i]+num[i+1:], new_list)

    def permute(self, num):
        num.sort()
        self._permute(num,[])
        return self.res

solution = Solution()
res = solution.permute([1,1,1,2])
# for i in range(len(res)):
#     print i, res[i]
#
# for key in solution.hash_table.keys():
#     print key
# print len(solution.hash_table)


