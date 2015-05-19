#Slow !!!
# class Solution:
#     # @param a list of integers
#     # @return an integer
#     def removeDuplicates(self, A):
#         if len(A) == 0:
#             return 0
#         temp = A[0]
#         n = 1
#         for num in A[1:]:
#             if num != temp:
#                 temp = num
#                 A[n] = num
#                 n += 1
#
#             #else:
#             #    A.remove(num)
#                 #A = A[:n-1] + A[n:]
#         A = A[:n]
#         return n, A
import gc


# class Solution:
#     #@param a list of integers
#     #@return an integer
#     def removeDuplicates(self, A):
#         if not A:
#             return 0
#         p = 1#position of the last unique element
#         for i in range(1,len(A)):
#             if A[i] != A[i-1]:
#                 A[p] = A[i]
#                 p += 1
#         A.extend(A[:p])
#         #A.append('zzz')
#         return p



















#With reference we can change the outer scope
# class Solution:
#     #@param a list of integers
#     #@return an integer
#     def removeDuplicates(self, A):
#         B = A[0]
#         if not B:
#             return 0
#         p = 0
#         for i in range(1,len(B)):
#             if B[i] != B[p]:
#                 p += 1
#                 B[p] = B[i]
#         p += 1
#         B = B[:p]
#         A[0] = B
#         return p
#
#
# s = Solution()
# my_A = [1,2,2,2,3,4,5,5,6,6,7]
# A = [my_A]
# print A
# print s.removeDuplicates(A)
# print A

# class PassByReference:
#     def __init__(self):
#         self.variable = 'Original'
#         self.Change(self.variable)
#         print self.variable
#
#     def Change(self, var):
#         var = 'Changed'
#
# pa = PassByReference()
# s = 'xx'
# pa.Change(s)
# print s



class Solution:
    #@param a list of integers
    #@return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        p = 0
        for i in range(1,len(A)):
            if A[i] != A[p]:
                p += 1
                A[p] = A[i]
        p += 1
        return p

s = Solution()
gc.get_objects()

A = [1,2,2,2,3,4,5,5,6,6,7]

print s.removeDuplicates(A)
print A


