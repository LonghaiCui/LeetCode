class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        start = -1
        length = 0
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        #Binary search
        # left = 0
        # right = len(nums) - 1
        #
        # while left < right:
        #     temp = (left + right)/2
        #     if target > nums[temp]:
        #         left = temp + 1
        #     else:
        #         right = temp
        # end = temp
        for i in range(len(nums) - start - 1):
            if nums[start + i + 1] == target:
                length += 1
        res = [start, start + length]
        return res


solution = Solution()
print solution.searchRange([5, 7, 7, 8, 8, 10], 8)
