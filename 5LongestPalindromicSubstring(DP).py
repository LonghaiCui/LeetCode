__author__ = 'longhaicui'
# Definition for singly-linked list.

#Dynamic Programming Time O(n2) Space O(n2) http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
#Odd Even            Time O(n2) Space O(1)  http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
#Manacher            Time O(n)              http://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-2/


#DP
class Solution:
    # @param s, a string
    # @return a string
    def longestPalindrome(self, s):
        len_s = len(s)
        matrix = [[0 for x in range(len_s)] for x in range(len_s)]
        max_len = 1
        start = 0
        for i in range(len_s):
            matrix[i][i] = 1

        for i in range(i-1):
            if s[i] == s[i+1]:
                matrix[i][i+1] = 1
                start = i
                max_len = 2

        #check for substring in length
        for sub_len in range(3, len_s+1):
            #check for substring start index
            for i in range(len_s):
                j = i + sub_len -1
                if i + sub_len > len_s:
                    break
                if s[i] == s[j] and matrix[i + 1][j-1] == 1:
                    matrix[i][j] = 1
                    max_len = sub_len
                    start = i

        return s[start: start + max_len]
solution = Solution()


#print solution.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv")
print solution.longestPalindrome("xabcbayyabcdcbaXYZZYX")
print solution.longestPalindrome("abcdcba")