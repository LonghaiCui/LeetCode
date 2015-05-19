#This is wrong
#First of all It's combination, permutation
#Second, it's too slow!
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def _combine(self, k, nums, determined, ret):
        if len(determined) == k:
            ret.append(determined)
            return
        for i in range(len(nums)):
            self._combine(k, nums[:i]+nums[i+1:],determined+[nums[i]], ret)

    def combine(self, n, k):
        if n < 1 or k < 1 or k > n:
            return
        nums = [x for x in range(1, n+1)]
        ret = []
        self._combine(k, nums, [], ret)
        return ret


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def _combine(self, n, k, hash_table, determined, ret):
        if len(determined) == k:
            ret.append(determined)
            return
        for i in range(1, n+1):
            if hash_table[i]:
                hash_table[i] = 0
                self._combine(n, k, hash_table, determined+[i], ret)
                hash_table[i] = 1

    def combine(self, n, k):
        if n < 1 or k < 1 or k > n:
            return
        #nums = [x for x in range(1, n+1)]
        hash_table = {}
        for i in range(1, n+1):
            hash_table[i] = 1
        ret = []
        self._combine(n, k, hash_table, [], ret)
        #return ret
        return len(ret)


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def _combine(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        ret = []
        for i in range(len(nums)):
            l = [[nums[i]] + x for x in self._combine(nums[:i]+nums[i+1:])]
            ret.extend(l)
        return ret

    def combine(self, n, k):
        if n < 1 or k < 1 or k > n:
            return
        nums = [x for x in range(1, n+1)]
        return self._combine(nums)


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def _combine(self, nums, k):
        if len(nums) == k:
            #print [[x] for x in nums]
            return [[x] for x in nums]
        ret = []
        for i in range(len(nums)):
            l = [[nums[i]] + x for x in self._combine(nums[:i]+nums[i+1:], k)]
            ret.extend(l)
        return ret

    def combine(self, n, k):
        if n < 1 or k < 1 or k > n:
            return
        nums = [x for x in range(1, n+1)]
        k = n - k + 1
        return self._combine(nums, k)


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def _combine(self, nums, k):
        if len(nums) == k:
            print [[x] for x in nums]
            return [[x] for x in nums]
        ret = []
        for i in reversed(range(len(nums))):
            for x in self._combine(nums[:i]+nums[i+1:], k):
                if nums[i] < x[0]:
                    ret.append([nums[i]]+x)
        return ret

    def combine(self, n, k):
        if n < 1 or k < 1 or k > n:
            return
        nums = [x for x in range(1, n+1)]
        k = n - k + 1
        return self._combine(nums, k)

# class Solution:
#     # @param {integer} n
#     # @param {integer} k
#     # @return {integer[][]}
#     def _combine(self, k, nums, determined, ret):
#         if len(determined) == k:
#             ret.append(determined)
#             return
#         for i in range(len(nums)):
#             self._combine(k, nums[i+1:],determined+[nums[i]], ret)
#
#     def combine(self, n, k):
#         if n < 1 or k < 1 or k > n:
#             return
#         nums = [x for x in range(1, n+1)]
#         ret = []
#         self._combine(k, nums, [], ret)
#         return ret


#Not work for n>= 10
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def _combine(self, start, n, k, ret, determined):
        if len(determined) == k:
            ret.append(determined)
            #print id(start)
            return
        for num in range(start, n+1):
            self._combine(num+1, n, k, ret, determined+[num])

    def combine(self, n, k):
        if n < 1 or k < 1 or k > n:
            return
        ret = []
        self._combine(1, n, k, ret, [])
        return ret


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        combo = [[]]
        for i in range(1, n+1):
          new_list = [j[:] for j in combo if len(j) < k]
          for j in new_list:
            j.append(i)
          combo.extend(new_list)
        return [j for j in combo if len(j) == k]



class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}

    def combine(self, n, k):
        if n < 1 or k > n:
            return
        if k == 1:
            return [[x] for x in range(1, n+1)]
        ret = []
        for x in self.combine(n, k-1):
            for i in range(1, x[0]):
                ret.append([i]+x)
        return ret


solution = Solution()
print solution.combine(4,3)
#print solution.combine(10,2)

