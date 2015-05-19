__author__ = 'longhaicui'

# O(n2) runtime, O(1) space – Brute force:
#
# The brute force approach is simple. Loop through each element x and find if there is another value that equals to target – x. As finding another value requires looping through the rest of array, its runtime complexity is O(n2).
#
# O(n) runtime, O(n) space – Hash table:
#
# We could reduce the runtime complexity of looking up a value to O(1) using a hash map that maps a value to its index


# 1. in hash_table (Keys not Values)
# 2. number in key, index in value

#key    value
# 2     1
# 7     2
# 11    3
# 15    4

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_table = {}
        for i in range(len(num)):
            if target - num[i] not in hash_table:
                hash_table[num[i]] = i + 1
            else:
                return hash_table[target - num[i]], i + 1

solution = Solution()
print solution.twoSum([2,7,11,15], 9)


#Brute force
#Time n2 Space 1

# class Solution:
#     # @return a tuple, (index1, index2)
#     def twoSum(self, num, target):
#         # return -1, -1
#         n = len(num)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if num[i] + num[j] == target:
#                     #print num[i], num[j],target
#                     #print "index1 = %d, index2 = %d" % (i+1, j+1)
#                     return i+1, j+1


# Hash table
#Time n space n

# class Solution:
#     # @return a tuple, (index1, index2)
#     # 8:42
#     def twoSum(self, num, target):
#         map = {}
#         for i in range(len(num)):
#             if num[i] not in map.keys():
#                 map[target - num[i]] = i + 1
#             else:
#                 return map[num[i]], i + 1
#
#         return -1, -1
#