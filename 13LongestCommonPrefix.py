class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        str = strs[0]
        res = ''
        for i in range(len(str)):
            for j in range(1,len(strs)):
                if i > len(strs[j]) - 1:
                    return res
                if str[i] != strs[j][i]:
                    return res
            res += str[i]
        return res
solution = Solution()
print solution.longestCommonPrefix(['abc','abcd','abc','abcd','abcde'])
