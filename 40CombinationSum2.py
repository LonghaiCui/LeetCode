class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def _combinationSum2(self, candidates, remained, cur_list, start, determined):
        if remained == 0:
            new_list = list(cur_list)
            determined.append(new_list)
        else:
            for i in range(start,len(candidates)):
                if i != start and candidates[i] == candidates[i-1]:
                    continue
                if remained >= candidates[i]:
                    new_list = list(cur_list)
                    new_list.append(candidates[i])
                    self._combinationSum2(candidates, remained-candidates[i], new_list, i+1, determined)

    def combinationSum2(self, candidates, target):
        candidates.sort()
        determined = []
        cur_list = []

        self._combinationSum2(candidates,target,cur_list,0, determined)
        return determined


# class Solution:
#     def combinationSum2(self, candidates, target):
#         candidates.sort()
#         return self.search(candidates, 0 ,target)
#
#     def search(self, candidates, start, target):
#         if target==0:
#             return [[]]
#         res=[]
#         for i in xrange(start,len(candidates)):
#             if i!=start and candidates[i]==candidates[i-1]:
#                 continue
#             if candidates[i]>target:
#                 break
#             for r in self.search(candidates, i+1, target-candidates[i]):
#                 res.append([candidates[i]]+r)
#         return res




solution = Solution()
print solution.combinationSum2([10,1,2,7,6,1,5],8)

# candidates = [1,2,3]
#
# print candidates[:1]+candidates[1+1:]


#Special case!!!
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0 ,target)

    def search(self, candidates, start, target):
        if target==0:
            return [[]]
        res=[]
        for i in xrange(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            for r in self.search(candidates, i+1, target-candidates[i]):
                res.append([candidates[i]]+r)
        return res