def _addBinary(a, b):
            c = ''
            add = 0
            len_a = len(a)
            len_b = len(b)
            for i in range(1,len_b+1):
                cur_value = int(a[-i]) + int(b[-i]) + add
                add = cur_value/2
                cur_value %= 2
                c = str(cur_value) + c
            if add == 0:
                print 'a'
                return a[:len_a-len_b] + c #10+1=11
            print 'a', a[:len_a-len_b]
            for i in reversed(range(len_a-len_b)):
                print 'a', a[i]
                if a[i] == '0':
                    print 'b'
                    return a[:i] + '1' + c #111,001+11=111,100
                c = '0' + c
            print 'c'
            return '1'+ c #11+1=100

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a
        return _addBinary(a, b) if len(a) > len(b) else _addBinary(b, a)

solution = Solution()
print solution.addBinary("101111", "10")
# "101111", "10"
# Output:	"1000001"
# Expected:	"110001"
