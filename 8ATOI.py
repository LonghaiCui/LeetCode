__author__ = 'longhaicui'

#Missed cases
#1. ''  -> 0
#2. '+1'-> 1
#3  '010' -> 10
#4   "    010" ->10
#5  ' -0012a42'->-12
#   [    -pow(2,31)  ,  pow(2,31)    )

def inRange(result,flag):
    if result > pow(2,31)-1 and flag == 1:
        result = pow(2,31)-1
    elif result > pow(2,31) and flag == -1:
        result = pow(2,31)
    return result * flag

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        hash_table = {
            '0': 1,
            '1': 1,
            '2': 1,
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 1,
            '8': 1,
            '9': 1,
        }
        size = len(str)
        start = 0
        for i in range(size):
            if str[i] == ' ':
                start += 1
            if str[start] in hash_table:
                break

        str = str[start:]

        if str == '':
            return 0
        if str[0] not in hash_table and str[0] != '-' and str[0]!='+':
            return 0

        result = 0
        flag = 1

        if str[0] == '-':
            flag = -1
        elif str[0] == '+':
            result = 0
        else:
            result = int(str[0])

        for i in range(1, len(str)):


            if str[i] not in hash_table:
                return inRange(result, flag)

            if str[i]!=' ':
                result = result * 10 + int(str[i])

        return inRange(result, flag)


solution = Solution()
print solution.myAtoi('-2147483649')


#1. ''  -> 0
#2. '+1'-> 1
#3  '010' -> 10
#4   "    010" ->10
#5  ' -0012a42'->-12

