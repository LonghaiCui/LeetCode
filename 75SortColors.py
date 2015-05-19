class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        red = 0
        white = 0
        blue = 0
        for num in nums:
            if num == 0:
                red += 1
                continue
            if num == 1:
                white += 1
                continue
            if num == 2:
                blue += 1
        mid_point1 = red
        mid_point2 = red + white
        for i in range(mid_point1):
            nums[i] = 0
        for i in range(mid_point1,mid_point2):
            nums[i] = 1
        for i in range(mid_point2,len(nums)):
            nums[i] = 2
        return nums

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        mid_point1 = 0
        mid_point2 = len(nums)-1
        for num in nums:
            if num == 0:
                nums[mid_point1] = 0
                mid_point1 += 1
                continue
            if num == 2:
                if nums[mid_point2] == 0:
                    mid_point1 += 1
                    if nums[mid_point1] == 2:
                        nums[mid_point1] = 0

                nums[mid_point2] = 2
                mid_point2 -= 1
        for i in range(mid_point1, mid_point2+1):
            nums[i] = 1
        print nums

solution = Solution()
#print solution.sortColors([0,2,0,1,2,0,1,1,1,2,1,2])

solution.sortColors([2,0])


