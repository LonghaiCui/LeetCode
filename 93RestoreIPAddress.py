class Solution:
    # @param {string} s
    # @return {string[]}
    def _restoreIpAddresses(self, s, n, determined, ret):
        if n == 0 and s:
            if s == '0' or (s[0] != '0' and int(s) < 256):
                ret.append(determined + s)
            return
        for i in range(1, 4):
            current = s[:i]
            if s:
                if current == '0' or (current[0] != '0' and int(current) < 256):
                    self._restoreIpAddresses(s[i:], n-1, determined + current + '.', ret)

    def restoreIpAddresses(self, s):
        ret = []
        self._restoreIpAddresses(s, 3, '', ret)
        return ret
solution = Solution()
print solution.restoreIpAddresses("010010")
