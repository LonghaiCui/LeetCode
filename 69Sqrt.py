class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        cur = x
        two_pos = []
        while cur > 100:
            remainder = cur % 100
            two_pos.append(remainder)
            cur /= 100
        #for i, cur_num in enumerate(reversed(two_pos)):
        #    print i, cur_num
        ret = 0
        original = 0
        two_pos.append(cur)
        two_pos.reverse()
        print two_pos
        for num in two_pos:
            print num
            cur_ret = ret * 10
            original = original * 100 + num
            for i in range(1, 11):
                if pow(cur_ret + i, 2) > original:
                    ret = cur_ret + i - 1
                    break
            print ret
        return ret

solution = Solution()
print solution.mySqrt(40000)

