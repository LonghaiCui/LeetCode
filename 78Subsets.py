class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        #ret = set()
        #ret.add((1,2))
        #return [list(x) for x in list(ret)]
        if not nums:
            return [[]]

        ret = set()
        for i in range(len(nums)):
            for x in range(self.subsets(nums[:i]+nums[i+1:])):
                ret.add(tuple(x))
        return [list(x) for x in list(ret)]

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def _subsets(self,nums,ret):
        if len(nums) == 2:
            ret.add(tuple(nums))
            return
        for i in range(len(nums)):
            ret.add(tuple(nums[:i]+nums[i+1:]))
            self._subsets(nums[:i]+nums[i+1:],ret)


    def subsets(self, nums):
        ret = set()
        self._subsets(nums,ret)

        new_ret = [list(x) for x in list(ret)]
        ret = set()
        for num in nums:
            ret.add(num)
        ret = [[x] for x in ret]

        ret.extend(new_ret)
        ret.extend([[],nums])
        return len(ret)


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def _subsets(self, nums, ret):
        if len(nums) == 2:
            ret.add(tuple(nums))
            return
        #ret.add(tuple(nums))
        for i in range(len(nums)):
            print 'ret', ret
            for cur in ret:
                print 'cur', cur
            ret.add(tuple(nums[:i]+nums[i+1:]))
            self._subsets(nums[:i]+nums[i+1:],ret)


    def subsets(self, nums):
        ret = set()
        self._subsets(nums,ret)

        new_ret = [list(x) for x in list(ret)]
        ret = set()
        for num in nums:
            ret.add(num)
        ret = [[x] for x in ret]

        ret.extend(new_ret)
        #ret.extend([[],nums])
        return ret
#
# solution = Solution()
# print solution.subsets([1,2,3])
# print solution.subsets([1,2,3,4,5,6,7,8,10,0])

# print tuple([1,2])
# a = set([0,0])
# a.add(1)
# a.add(2)
#
# b = set()
# b.add(5)
# for i in a:
#     print i, type(i)
# print


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def _subsets(self, nums, ret, determined, prev):
        if len(determined) > len(nums)- 2:
            return

        for i in range(len(nums)):
            if nums[i] > prev:


                ret.append(determined+[nums[i]])
                ret.append(nums[:i]+nums[i+1:])
                if len(determined) != len(nums) - 2:
                    # ret.append(determined+[nums[i]])
                    # ret.append(nums[:i]+nums[i+1:])
                    # return
                    self._subsets(nums[:i]+nums[i+1:], ret, determined+[nums[i]], nums[i])

    def subsets(self, nums):
        if not nums:
            return [[]]
        #nums.sort()
        ret = list()
        ret.append([])
        ret.append(nums)
        self._subsets(nums, ret, [], 0)
        return ret

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if S == []:
            return []
        S.sort() #sort the array to avoid descending list of int
        res=[[]]
        for element in S:
            temp = []
            for ans in res:
                 #append the new int to each existing list
                temp.append(ans+[element])
            res += temp
        return res

#solution = Solution()
#print solution.subsets([1,2,3,4])

class Solution:
    def subsets(self, nums):
        if not nums:
            return []
        nums.sort()
        result = [[]]
        for num in nums:
            cur_result = []
            for ret in result:
                cur_result.append(ret+[num])
            result.extend(cur_result)
        return result

solution = Solution()
print solution.subsets([1,2,3,4])
#print solution.subsets([1,2,3,4,5,6,7,8,10,0])
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]