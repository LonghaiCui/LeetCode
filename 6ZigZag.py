class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        #Negtive number is not Palindrome
        if x < 0:
            return False

        n = 0
        y = x
        while y > 0:
            n += 1
            y /= 10
        y = x
        for i in range(n/2):
            x1 = y % 10
            x2 = x / pow(10, n - i - 1) % 10
            print x1, x2
            if x1 != x2:
                return False
            y /= 10
        return True
solution = Solution()
print solution.isPalindrome(-2147483648)
#print solution.longestPalindrome("abcdcba")


