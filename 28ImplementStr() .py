class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        n = len(needle)
        pos = 0
        while haystack:
            cur_str = haystack[:n]
            if len(cur_str) != n:
                return -1
            if cur_str == needle:
                return pos
            haystack = haystack[1:]
            pos += 1
        return -1

s = Solution()
print s.strStr('','')
