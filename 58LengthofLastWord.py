class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        end = -1
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                end = i
                break
        for i in reversed(range(end)):
            if s[i] == ' ':
                return end - i
        return end + 1 if end >= 0 else 0


solution = Solution()
print solution.lengthOfLastWord('Here is some kk   ')

print solution.lengthOfLastWord('Here is some kk')