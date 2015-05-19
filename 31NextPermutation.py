#for i=2 -> len(num)
#    for j = first right to i-1:
#        if a[j]> ith right

#1.Bad   put a[j] to a[i]
#        move all the elements 1 position back
#        sort right elements
#This has a problem -> sort need extra space,
#Missed observation -> if found, it will be biggest number after switch
# since all the checked elements are greater than current element

#2. Good
#        Switch i and j,
#        reverse right elements


class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        length = len(num)
        descending = 1
        for i in range(length-1):
            if num[i] < num[i+1]:
                descending = 0
                break
        if descending:
            num.reverse()
            print num
            return num
        for i in range(1,length):
            for j in range(i):
                #print i , j, num[::-1][j], num[::-1][i]
                if num[::-1][j] > num[::-1][i]:
                    #print i , j, num[::-1][j], num[::-1][i]
                    temp = num[length-1-i]
                    num[length-1-i] = num[length-1-j]
                    num[length-1-j] = temp
                    #print num[length-1-i] ,num[length-1-j]
                    #Wrong num = num[:length-i-1] + num[length-i:][::-1]
                    num = num[:length-i] + num[length-i:][::-1]
                    print num
                    return






# class Solution:
#     # @param num, a list of integer
#     # @return nothing (void), do not return anything, modify num in-place instead.
#     # 1:23
#     def nextPermutation(self, num):
#         for i in range(len(num) - 2, -1, -1):
#             for j in range(len(num) - 1, i, -1):
#                 if num[i] < num[j]:
#                     num[i], num[j] = num[j], num[i]
#                     num[i+1:] = num[i+1:][::-1]
#                     print num
#                     return
#
#         num.reverse()
#         print num

solution = Solution()
solution.nextPermutation([1,2,3,4])
solution.nextPermutation([1,2,5,4])
solution.nextPermutation([1,2,7,4])
solution.nextPermutation([1,6,5,4])
solution.nextPermutation([1,6,7,4])
solution.nextPermutation([1,3,2])

[1, 2, 4, 3]
[1, 4, 2, 5]
[1, 4, 2, 7]
[4, 1, 5, 6]
[1, 7, 4, 6]

#print solution.nextPermutation([4,3,2,1])


# l= [1,2]
# l2 = [-1,3]
# print l + l2

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num)-2, -1, -1):
            for j in range(len(num)-1, i, -1):
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
                    return num[:i+1]+num[:i:-1]

        return num[::-1]

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    # 1:23
    def nextPermutation(self, num):
        for i in range(len(num) - 2, -1, -1):
            for j in range(len(num) - 1, i, -1):
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
                    num[i+1:] = num[i+1:][::-1]
                    return

        num.reverse()


class Solution:
    def reverse(self, arr, i, j):
        while(i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        n = len(num)

        if(n == 1):
            return

        i = n-1
        while( i > 0 and num[i-1] >= num[i] ):
            i -= 1

        if( i <= 0):
            self.reverse(num, 0, n-1)
            return

        j = n - 1
        while( num[j] <= num[i-1] ):
            j -= 1

        num[i-1], num[j] = num[j], num[i-1]

        self.reverse(num, i, n-1)