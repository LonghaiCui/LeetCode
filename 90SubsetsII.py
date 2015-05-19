class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        ret = [[]]
        for num in nums:
            # for ele in ret: #No
            #     ret.append(ele + [num])
            for i in range(len(ret)): #Yes
                ret.append(ret[i] + [num])
            # for i, ele in enumerate(reversed(ret)): #Yes
            #     ret.append(ret[i] + [num])
        return ret
        pass

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        ret = set()
        ret.add(tuple([]))
        for num in nums:
            new_set = set()
            for i, ele in enumerate(ret):
                new_ele = tuple(list(ele) + [num])
                new_set.add(new_ele)
            #print new_set
            ret = ret | new_set
        return [list(x) for x in ret]

#Please tell me why this is wrong answer
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, s):
        def dfs(cur, s, path):
            ret.append(path)
            for i in range(cur, len(s)):
                if i > cur and s[i] == s[i-1]: continue
                dfs(i+1, s, path + [s[i]])

        s.sort()
        ret = []
        dfs(0, s, [])
        return ret
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        ret = [[]]
        for num in nums:
            # for ele in ret: #No
            #     ret.append(ele + [num])
            for i in range(len(ret)): #Yes
                ret.append(ret[i] + [num])
            # for i, ele in enumerate(reversed(ret)): #Yes
            #     ret.append(ret[i] + [num])
        return ret
        pass

solution = Solution()
print solution.subsetsWithDup([1,2,2])

[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
# 0#0
# 1#1
#
# 00#0
# 01#1
# 11#3
# 10#2
#
# 000#0
# 001#1
# 011#3
# 010#2
# 110#6
# 111#7
# 101#5
# 100#4
#
# 0000#0 +1
# 0001#1 +2
# 0011#3 -1
# 0010#2 +4
# 0110#6 +1
# 0111#7 -2
# 0101#5 -1
# 0100#4 +8
# 1100#12 +1
# 1101#13 +2
# 1111#15 -1
# 1110#14 -4
# 1010#10 -1
# 1011#11 -2
# 1001#9 -1
# 1000#8
#
# [[]]
# [[][1]]
#
# [[][1][2][12][3][13][23][123]]
# [[][1][2][12][2][12][22][122]]
#
# [[][1][2][12]]
# [[][1][2][12][22][122]]
# [[2][12][22][122][22][222][1222]]
#
# [[3][13][23][123][23][223][1223]]