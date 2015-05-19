class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}

    def _getPermutation(self, nums, determined, ret):
        if not nums:
            ret.append(determined)
            return
        for i in range(len(nums)):
            self._getPermutation(nums[:i]+nums[i+1:], determined+nums[i], ret)

    def getPermutation(self, n, k):
        max_size = 1
        for i in range(1, n+1):
            max_size *= i
        if k > max_size:
            return
        nums = [str(x+1) for x in range(n)]
        ret = []
        self._getPermutation(nums, '', ret)
        return ret


#Using recursion list nums, Still to slow with the recursion break additional condition
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self, k=0, ret=[], ele=''):
        self.k = k
        self.ret = ret
        self.ele = ele

    def _getPermutation(self, nums, determined):
        if not nums and self.k > 0:
            self.ret.append(determined)
            if len(self.ret) == self.k:
                self.ele = determined
                self.k = -1
        for i in range(len(nums)):
            self._getPermutation(nums[:i]+nums[i+1:], determined+nums[i])

    def getPermutation(self, n, k):
        max_size = 1
        for i in range(1, n+1):
            max_size *= i
        if k > max_size:
            return
        nums = [str(x+1) for x in range(n)]
        self.k = k
        self._getPermutation(nums, '')
        #print self.ret
        return self.ele
# solution = Solution()
# print solution.getPermutation(9, 24)
#print solution.getPermutation(9, 94626)
#Using recursion dictionary hash_table
#Too Slow!
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self, k=0, n=0, ret=[], ele=''):
        self.k = k
        self.n = n
        self.ret = ret
        self.ele = ele

    def _getPermutation(self, hash_table, determined):
        if len(determined) == self.n and self.k > 0:
            #print determined
            self.ret.append(determined)
            if len(self.ret) == self.k:
                self.ele = determined
                self.k = -1
        for i in range(1, self.n+1):
            if hash_table[i] == 1:
                hash_table[i] = 0
                self._getPermutation(hash_table, determined+str(i))
                hash_table[i] = 1

    def getPermutation(self, n, k):
        max_size = 1
        for i in range(1, n+1):
            max_size *= i
        if k > max_size:
            return
        hash_table = {}
        for i in range(1, n+1):
            hash_table[i] = 1
        self.k = k
        self.n = n
        self._getPermutation(hash_table, '')
        return self.ele


#Thinking opposite way,
#Generate number from back to front
#No, when k is too big, still too long!
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self, k=0, ret=[], ele=''):
        self.k = k
        self.ret = ret
        self.ele = ele

    def _getPermutation(self, nums, determined):
        if not nums and self.k > 0:
            #print determined
            self.ret.append(determined)
            if len(self.ret) == self.k:
                self.ele = determined
                print determined
                self.k = -1
        for i in range(len(nums)):
            self._getPermutation(nums[:i]+nums[i+1:], determined+nums[i])

    def getPermutation(self, n, k):
        max_size = 1
        x = 0
        for i in range(2, n+1):
            max_size *= i
            if k > max_size:
                x = i + 1
        if k > max_size:
            return
        prev = ''
        for i in range(1, n-x+1):
            prev += str(i)
        nums = [str(y) for y in range(n-x+1, n+1)]
        print prev, x, nums
        self.k = k
        self._getPermutation(nums, '')
        return prev + self.ele


#Thinking opposite way,
#Generate number from back to front
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self, k=0, remained=''):
        self.k = k
        self.remained = remained

    def _getPermutation(self, nums, determined):
        if not nums and self.k > 0:
            self.k -= 1
            if self.k == 0:
                self.remained = determined
        for i in range(len(nums)):
            self._getPermutation(nums[:i]+nums[i+1:], determined+nums[i])

    def getPermutation(self, n, k):
        max_size = 1
        x = 0
        for i in range(2, n+1):
            max_size *= i
            if k > max_size:
                x = i + 1
        if k > max_size:
            return
        start = ''
        for i in range(1, n-x+1):
            start += str(i)
        nums = [str(y) for y in range(n-x+1, n+1)]
        self.k = k
        self._getPermutation(nums, '')
        return start + self.remained

solution = Solution()
print solution.getPermutation(9, 24)
print solution.getPermutation(9, 94626)

#This time decide number in each position 1 by 1
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        divider = 1
        for i in range(2, n):
            divider *= i
        if k > divider * n:
            return
        ret = ''
        nums = [x+1 for x in range(n)]
        for i in range(n-1):
            pos = (k-1)/divider
            ret += str(nums[pos])
            nums = nums[:pos] + nums[pos+1:]
            # cur_ele = nums[(k-1)/divider]
            # ret += str(cur_ele)
            # nums.remove(cur_ele)
            #if k==0 improve here
            k %= divider
            if k == 0:
                for num in reversed(nums):
                    ret += str(num)
                return ret
            divider /= (n-i-1)
        return ret + str(nums[0])


# solution = Solution()
# print solution.getPermutation(9, 94626)
# print [1,2,3,4]
# 348567921
#by reducing the depth of recursion
# for i in range(94626):
#     x = i
#
# print x

