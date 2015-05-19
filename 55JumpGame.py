#Try recursion first
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def _canJump(self, nums, cur_pos):
        for i in range(nums[cur_pos]):
            if cur_pos + nums[cur_pos + i] >= len(nums):
                return True
        if self._canJump(nums, cur_pos + i):
            return True

    def canJump(self, nums):
        for i in range(len(nums)):
            return self._canJump(nums, i)

#Try DP O(n)
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        globe_max = 0
        for i in xrange(len(nums)):
            if i <= globe_max:
                cur_max = nums[i] + i
                if cur_max >= len(nums)-1:
                    return True
                if cur_max >= globe_max:
                    globe_max = cur_max
        return False


#Try DP O(n)
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        globe_max = 0
        n = len(nums)
        for i in xrange(len(nums)):
            if i <= globe_max:
                if nums[i] + i >= n - 1:
                    return True
                globe_max = max(globe_max, nums[i] + i)
        return False


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        globe_max = 0
        n = len(nums)
        for (key, value) in enumerate(nums):
            if key <= globe_max:
                cur_max = value + key
                if cur_max >= n - 1:
                    return True
                globe_max = max(globe_max, cur_max)
        return False

solution = Solution()
print solution.canJump([1,2,3])

