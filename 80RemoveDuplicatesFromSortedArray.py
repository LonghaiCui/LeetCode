class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        pos = 1
        count = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
                if count <= 2:
                    nums[pos] = nums[i]
                    pos += 1

            else:
                count = 1
                current = nums[pos] = nums[i]
                pos += 1
        print nums
        return pos

solution = Solution()
print solution.removeDuplicates([1,1,1,1,2,3,3,4,4,4,5])