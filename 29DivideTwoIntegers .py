class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):

        flag = True
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            flag = False
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == dividend:
            return 1 if flag else -1
        if divisor > dividend:
            return 0




        if divisor == 1:
            if dividend == pow(2,31) and flag:
                return dividend-1
            return dividend if flag else -dividend
        hash_table = {}
        n = 0
        while pow(divisor,n) < dividend:
            n += 1
        low_pow = pow(divisor, n-1)
        while dividend >= divisor:
            cur_num = 0
            while dividend >= low_pow and n > 0:
                dividend -= low_pow
                cur_num += 1
            n -= 1
            low_pow = pow(divisor, n-1)
            if cur_num != 0:
                hash_table[low_pow] = cur_num
        print hash_table
        res = 0
        for key in hash_table.keys():
            while hash_table[key] != 0:
                res += key
                hash_table[key] -= 1
        if flag:
            return res
        else:
            return -res
s = Solution()
print s.divide(78,3)

#
# Input:	-2147483648, -1
# Output:	2147483648
# Expected:	2147483647

# Basic idea: a/b = e^(ln(a))/e^(ln(b)) = e^(ln(a)-ln(b))
# class Solution {
# public:
#     int divide(int dividend, int divisor) {
#         if (dividend==0) return 0;
#         if (divisor==0) return INT_MAX;
#         long long res=double(exp(log(fabs(dividend))-log(fabs(divisor))));
#         if ((dividend<0)^(divisor<0)) res=-res;
#         if (res>INT_MAX) res=INT_MAX;
#         return res;
#     }
# };

# for example, if we want to calc (17/2)
#
# ret = 0;
#
# 17-2 ,ret+=1; left=15
#
# 15-4 ,ret+=2; left=11
#
# 11-8 ,ret+=4; left=3
#
# 3-2 ,ret+=1; left=1
#
# ret=8;
class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        isMinus= ((dividend<0 and divisor >0) or (dividend>0 and divisor <0));
        ret=0;
        dividend,divisor=abs(dividend),abs(divisor);
        c,sub=1,divisor;

        while(dividend >= divisor):
            if(dividend>=sub):
                dividend-=sub;
                ret+=c;
                sub=(sub<<1);
                c=(c<<1);
            else:
                sub=(sub>>1);
                c=(c>>1);

        if(isMinus):
            ret=-ret;
        return min(max(-2147483648,ret),2147483647);


class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


#https://leetcode.com/discuss/26352/share-my-46ms-python-code-without-shift-opperation-and-abs