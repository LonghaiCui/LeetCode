class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def _combinationSum(self, candidates, remained, cur_list, cur_num, determined):
        if remained < 0:
            return
        if remained == 0:
            new_list = list(cur_list)
            determined.append(new_list)
        else:
            for i in range(len(candidates)):
                if remained >= candidates[i] >= cur_num:
                    new_list = list(cur_list)
                    new_list.append(candidates[i])
                    self._combinationSum(candidates, remained-candidates[i], new_list, candidates[i], determined)

    def combinationSum(self, candidates, target):
        candidates.sort()
        determined = []
        cur_list = []
        self._combinationSum(candidates,target,cur_list,-1,determined)
        return determined
solution = Solution()
print solution.combinationSum([2,3,6,7],7)

class Solution:
# @param candidates, a list of integers
# @param target, integer
# @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        result=[]
        def backtracking(start,remaining,temp,result):
            if remaining<0:
                return
            if remaining==0:
                result.append(temp[:])
                return

            for i in range(start,len(candidates)):
                temp.append(candidates[i])
                backtracking(i,remaining-candidates[i],temp,result)
                temp.pop()

        backtracking(0,target,[],result)

        return result


class Solution:
# @param candidates, a list of integers
# @param target, integer
# @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for n in range(start, len(candidates)):
                t = total + candidates[n]
                if t > target:
                    break
                stack.append((t, n, res + [candidates[n]]))
        return result

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # 11:00
    def __init__(self):
        self.output = []

    def combinationSum(self, candidates, target, temp = None, pos = 0):
        if temp is None:
            candidates.sort()
        temp = temp or []

        if target == 0:
            self.output.append(temp[:])
            return

        for i in range(pos, len(candidates)):
            num = candidates[i]
            if target - num < 0:
                break

            temp.append(num)
            self.combinationSum(candidates, target - num, temp, i)
            temp.pop()

        return self.output