class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        i = int(num1)
        j = int(num2)
        k = i * j
        return str(k)

solution = Solution()
print solution.multiply('12','12')

