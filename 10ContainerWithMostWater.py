__author__ = 'longhaicui'
#First use list Then use dict to store current_max for each line
#O n solution where left++ right-- both direction for specific condition
class Solution:
    #@param {integer[]} height
    #@return {integer}
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = abs(right - left) * min(height[left], height[right])
        while left + 1 < right:#######
            if height[right] > height[left]:
                left += 1
                maxArea = max( maxArea, (right - left) * min(height[left], height[right]))
            else:
                right -= 1
                maxArea = max( maxArea, (right - left) * min(height[left], height[right]))
        return maxArea

#
# #O n2 Too slow
# class Solution:
#     # @param {integer[]} height
#     # @return {integer}
#     def maxArea(self, height):
#         maxArea = 0
#         for i in range(1, len(height)):
#             for j in range(i):
#                 maxArea = max(maxArea, (min(height[i],height[j]))*(i-j))
#         return maxArea


#Wrong Solution, from left to right only gives local max.
#max left  and max right can not meet with each other
# class Solution:
#     #@param {integer[]} height
#     #@return {integer}
#     def maxArea(self, height):
#         left = 0
#         right = 1
#         maxArea = min(height[left], height[right])
#         for i in range(2, len(height)):
#             if height[right] > height[left]:
#                 curArea = (i - right) * min(height[i], height[right])
#                 if curArea >= maxArea:
#                     maxArea = curArea
#                     left = right
#                     right = i
#         print left , right
#         return maxArea
solution = Solution()
print solution.maxArea([28,342,418,485,719])




#108 ms  Other people's solution
class Solution:
    # @return an integer
    def maxArea(self, height):
        area, left, right = 0, 0, len(height) - 1

        while left < right:
            area = max(area, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area