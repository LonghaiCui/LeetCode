class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        pos = m + n -1
        pos1 = m -1
        pos2 = n -1
        while pos1 > -1 and pos2 > -1:

            if nums1[pos1] > nums2[pos2]:
                nums1[pos] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[pos] = nums2[pos2]
                pos2 -= 1
            pos -= 1
        if pos2 > -1:
            for i in range(pos2+1):
                nums1[i] = nums2[i]
        print nums1


solution = Solution()
#solution.merge([1,3,4,6,-1,-1,-1],4,[2,5,-1,-1],2)
#solution.merge([1,2,4,5,6,0], 5, [3], 1)
solution.merge([2,0], 1, [1], 1
)
1,2,3,4,5,6,-1

-1,1,   2