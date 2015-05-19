class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        sign = 1 if x > 0 else -1
        x = abs(x)
        x = 1/float(x) if n < 0 else float(x)
        if n % 2 == 0:
            return sign * self.myPow(x * x, n/2)
        else:
            return sign * self.myPow(x * x, n/2) * x

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def _myPow(self,x,n):
        if n == 1:
            return x
        if n % 2 == 0:
            return self.myPow(x * x, n/2)
        else:
            return self.myPow(x * x, n/2) * x

    def myPow(self, x, n):
        if x == 0.0:
            return 0.0
        if n == 0:
            return 1.0
        if abs(x) == 1.0:
            return -1.0 if (x < 0 and n % 2 == 1) else 1.0
        if n < 0:
            return self._myPow(1/x,-n)
        else:
            return self._myPow(x,n)

solution = Solution()
print solution.myPow(1.00000, -2147483648)
print solution.myPow(34.00515, -3)
print solution.myPow(2.0, -3)
print solution.myPow(-4.48392, 6)
#print 1/2.0
