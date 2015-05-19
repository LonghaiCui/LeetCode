
class Solution:
    # @return an integer
    def  threeSumClosest(self, num, target):
        if not num:
            return []
        num = sorted(num)
        sum = 0
        min_diff = pow(2,31)-1
        for i1 in range(len(num)-2):
            i2 = i1 + 1
            i3 = len(num) - 1
            while i2 < i3:
                cur_sum = num[i1]+num[i2]+num[i3]
                cur_diff = target - cur_sum
                if abs(cur_diff) < abs(min_diff):
                    min_diff = cur_diff
                    sum = cur_sum
                if cur_diff < 0:
                    i3 -= 1
                else:
                    i2 += 1
        return sum


solution = Solution()
print solution.threeSumClosest([123,5,6,4,75,23,76,43,75,3],100)
