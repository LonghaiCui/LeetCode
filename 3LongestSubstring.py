__author__ = 'longhaicui'
# Definition for singly-linked list.


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        hash_table = {}
        max_length = 0
        start_index = 0
        for i in range(len(s)):
            #Current char need to be used AND be range of current longest substring
            #to be considered as new start index of possible new longest substring
            if s[i] in hash_table and start_index <= hash_table[s[i]]:
                #Need to see if the NEXT char is the start of the possible longest substring
                #NOT directly go to the current char
                start_index = hash_table[s[i]] + 1
            else:
                max_length = max(max_length, i - start_index + 1)
            hash_table[s[i]] = i
        return max_length
# class Solution:
#     # @return an integer
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
#
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)
#
#             usedChar[s[i]] = i
#
#         return maxLength, start















class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_len = 0
        start_pos = 0
        visited = {}
        for i in range(len(s)):
            if s[i] in visited and visited[s[i]] >= start_pos:
                start_pos = visited[s[i]] + 1
            else:
                max_len = max(max_len, i - start_pos + 1)
            visited[s[i]] = i
        return max_len


solution = Solution()
print solution.lengthOfLongestSubstring("dvdf")

