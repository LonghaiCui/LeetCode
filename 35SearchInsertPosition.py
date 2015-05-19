class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        length = len(nums)
        if target > nums[length-1]:
            return length
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) / 2
            if target > nums[mid]:
                if mid == length - 1:
                    return length
                if target < nums[mid+1]:
                    return mid + 1
                else:
                    left = mid + 1
            elif target < nums[mid]:
                if mid == 0:
                    return 0
                if target > nums[mid-1]:
                    return mid
                else:
                    right = mid - 1
            else:
                return mid
#Improve
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        length = len(nums)
        if target > nums[length-1]:
            return length
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) / 2
            if target > nums[mid]:
                if target < nums[mid+1]:
                    return mid + 1
                else:
                    left = mid + 1
            elif target < nums[mid]:
                if target > nums[mid-1]:
                    return mid
                else:
                    right = mid - 1
            else:
                return mid


solution = Solution()
print solution.searchInsert([5, 7, 8, 10], 1)
