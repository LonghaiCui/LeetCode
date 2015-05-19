class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if not digits:
            return
        digit = digits[-1] + 1
        pos = len(digits) - 1
        if digit != 10:
            return digits[:-1] + [digit]
        while digit == 10:
            digits[pos] = 0
            pos -= 1
            if pos == -1:
                return [1] + digits
            digit = digits[pos] + 1
        digits[pos] = digit
        return digits


class Solution:
        # @param {integer[]} digits
        # @return {integer[]}
        def plusOne(self, digits):
            digit = digits[-1] + 1
            if digit != 10:
                print 12
                return digits[:-1] + [digit] #12->13
            pos = len(digits) - 1
            while digit == 10 and pos > -1:
                digits[pos] = 0
                pos -= 1
                digit = digits[pos] + 1
            if pos == -1:
                print 99
                return [1] + digits #999->1000

            digits[pos] = digit
            print '1299'
            return digits #1299->1300

solution = Solution()
print solution.plusOne([1,2])

print solution.plusOne([9,9])
print solution.plusOne([1,2,9,9])
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num = 0
        for d in digits:
            num *= 10
            num += d

        num += 1
        output = []

        while num:
            temp = num % 10
            num /= 10
            output.append(temp)

        return output[::-1]

def plusOne(self, digits):
    digit = digits[-1] + 1
    if digit != 10:
        return digits[:-1] + [digit] #12->13
    pos = len(digits) - 1
    while digit == 10 and pos > -1:
        digits[pos] = 0
        pos -= 1
        digit = digits[pos] + 1
    if pos == -1:
        return [1] + digits #999->1000
    digits[pos] = digit
    return digits #1299->1300