class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0
        #A.sort()
        n = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[n] = A[i]
                n += 1
        A = A[:n]

        return n, A




s = Solution()
print s.removeElement([1,2,2,2,6,77,7,7,7],2)