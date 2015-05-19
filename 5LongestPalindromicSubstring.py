__author__ = 'longhaicui'
# Definition for singly-linked list.

#Dynamic Programming Time O(n2) Space O(n2) http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
#Odd Even            Time O(n2) Space O(1)  http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
#Manacher            Time O(n)              http://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-2/

class Solution:
    # @param s, a string
    # @return a string
    def longestPalindrome(self, s):
        odd_longest_wing = 0
        even_longest_wing = 0
        index_middle = 0

        length = len(s)
        #odd number
        for i in range(length):
            cur_longest_wing = 0
            for j in range(i):
                if i + j + 2 > length:
                    break
                #print i, j, s[i-j], s[i+j]
                if s[i-j-1] == s[i+j+1]:
                    cur_longest_wing += 1
                else:
                    break
            if odd_longest_wing < cur_longest_wing:
                odd_longest_wing = cur_longest_wing
                index_middle = i

        #even number
        for i in range(length):
            cur_longest_wing = 0
            for j in range(i+1):
                if i + j + 2 > length:
                    break
                #print i, j, s[i-j], s[i+j]
                if s[i-j] == s[i+1+j]:
                    cur_longest_wing += 1
                else:
                    break

            #Only when even wing length is bigger than odd wing length, even substring can be longer than odd substring
            #Because odd substring will be increased by 1 for the middle char
            if even_longest_wing < cur_longest_wing:
                even_longest_wing = cur_longest_wing
                index_middle_left = i

        if even_longest_wing > odd_longest_wing:
            print "Even"
            print index_middle_left, even_longest_wing
            return s[index_middle_left - even_longest_wing + 1: index_middle_left + even_longest_wing + 1]
        else:
            print "Odd"
            print index_middle, odd_longest_wing
            return s[index_middle - odd_longest_wing: index_middle + odd_longest_wing + 1]


solution = Solution()
print solution.longestPalindrome("xabcbayyabcdcbaXYZZYX")
#print solution.longestPalindrome("abcdcba")


