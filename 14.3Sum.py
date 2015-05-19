# O n2 Time limit exceed
# class Solution:
#     # @return a list of lists of length 3, [[val1,val2,val3]]
#     def threeSum(self, num):
#         if not num:
#             return []
#         num = sorted(num)
#         hash_table = {}
#         for i in range(len(num)):
#             if num[i] not in hash_table:
#                 hash_table[num[i]] = 1
#             else:
#                 hash_table[num[i]] += 1
#         res = set()
#         for i in range(len(num)):
#             for j in range(i+1,len(num)):
#                 hash_table[num[i]] -= 1
#                 hash_table[num[j]] -= 1
#                 wanted = -num[i]-num[j]
#                 if wanted in hash_table and hash_table[wanted] > 0:
#                     new = (num[i],num[j], wanted)
#                     #new.sort()
#                     res.add(new)
#                 hash_table[num[i]] += 1
#                 hash_table[num[j]] += 1
#         return [list(t) for t in res]


class Solution1:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        i,result = 0, set()
        #print num
        while i < len(num) - 2:
            j, k = i + 1, len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] == 0:
                    result.add((num[i], num[j],num[k]))
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
                else:
                    j += 1
            i+=1

        return [list(t) for t in result]
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if not num:
            return []
        num = sorted(num)
        res = []
        for i1 in range(len(num)-2):
            i2 = i1 + 1
            i3 = len(num) - 1
            while i2 < i3:
                cur_sum = num[i1]+num[i2]+num[i3]
                if cur_sum == 0:
                    if [num[i1],num[i2],num[i3]] not in res:
                        res.append([num[i1],num[i2],num[i3]])
                    i2 += 1
                elif cur_sum > 0:
                    i3 -= 1
                else:
                    i2 += 1
        return res


#Avoid duplication for the start, mid and end
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        num.sort()
        res = []
        for i in range(len(num)-2):
            #Avoid duplicated start
            if i > 0 and num[i] == num[i-1]:
                continue
            start_pos = i
            mid_pos = i+1
            end_pos = len(num) - 1
            while mid_pos < end_pos:
                #Avoid duplicated mid
                if mid_pos - 1 != start_pos and num[mid_pos] == num[mid_pos-1]:
                    mid_pos += 1
                    continue
                #Avoid duplicated end
                if end_pos+1 < len(num) and num[end_pos] == num[end_pos+1]:
                    end_pos -= 1
                    continue

                if num[start_pos] + num[mid_pos] + num[end_pos] == 0:
                    #No need to check duplication with set or not in
                    #if [num[start_pos], num[mid_pos], num[end_pos]] not in res:
                    #Speed up 766ms -> 246ms Good enough but code too long
                    res.append([num[start_pos], num[mid_pos], num[end_pos]])
                    mid_pos += 1



                if num[start_pos] + num[mid_pos] + num[end_pos] > 0:
                    end_pos -= 1
                else:
                    mid_pos += 1
        return res


#Preprocess the list 1. order 2. remove duplicates
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:

            return []
        num.sort()
        last_value = num[0]
        cur_pos = 0
        cur_num = 1
        num_0 = 0
        if last_value == 0:
            num_0 += 1
        for i in range(1, len(num)):
            if last_value != num[i]:
                cur_pos += 1
                num[cur_pos] = num[i]
                last_value = num[i]
                cur_num = 1
            elif last_value == num[i] and cur_num < 2:
                cur_pos += 1
                num[cur_pos] = num[i]
                last_value = num[i]
                cur_num += 1
            if num[i] == 0:
                num_0 += 1

        num = num[:cur_pos+1]
        #return num
        res = []
        for i in range(len(num)-2):
            #Avoid duplicated start
            if i > 0 and num[i] == num[i-1]:
                continue
            #This two lines can not be deleted
            #   if i > 0 and num[i] == num[i-1]:
            #   continue
#Because
#[-2,-2,0,2,4]
# 0 1 4
# 0 2 3
# 1 2 3
# [[-2, -2, 4], [-2, 0, 2], [-2, 0, 2]]
            start_pos = i
            mid_pos = i+1
            end_pos = len(num) - 1
            while mid_pos < end_pos:
                # #Avoid duplicated mid
                # if mid_pos - 1 != start_pos and num[mid_pos] == num[mid_pos-1]:
                #     mid_pos += 1
                #     continue
                # #Avoid duplicated end
                # if end_pos+1 < len(num) and num[end_pos] == num[end_pos+1]:
                #     end_pos -= 1
                #     continue

                if num[start_pos] + num[mid_pos] + num[end_pos] == 0:
                    #No need to check duplication with set or not in
                    #if [num[start_pos], num[mid_pos], num[end_pos]] not in res:
                    #Speed up 766ms -> 246ms Good enough but code too long
                    res.append([num[start_pos], num[mid_pos], num[end_pos]])
                    print start_pos, mid_pos, end_pos
                    mid_pos += 1

                if num[start_pos] + num[mid_pos] + num[end_pos] > 0:
                    end_pos -= 1
                else:
                    mid_pos += 1
        print 'num_0', num_0
        if num_0 >= 3:
            res.append([0,0,0])
        return res

test = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
#test = [-1,-1,-1,1]
test = [0,0,0]
test = [-2,-2,0,2,4]

solution = Solution()
#test1 = [[-15, 1, 14], [-15, 2, 13], [-15, 3, 12], [-15, 4, 11], [-15, 5, 10], [-15, 6, 9], [-15, 7, 8], [-14, 0, 14], [-14, 1, 13], [-14, 2, 12], [-14, 3, 11], [-14, 4, 10], [-14, 5, 9], [-14, 6, 8], [-14, 7, 7], [-13, -1, 14], [-13, 0, 13], [-13, 1, 12], [-13, 2, 11], [-13, 3, 10], [-13, 4, 9], [-13, 5, 8], [-13, 6, 7], [-12, -2, 14], [-12, -1, 13], [-12, 0, 12], [-12, 1, 11], [-12, 2, 10], [-12, 3, 9], [-12, 4, 8], [-12, 5, 7], [-12, 6, 6], [-11, -3, 14], [-11, -2, 13], [-11, -1, 12], [-11, 0, 11], [-11, 1, 10], [-11, 2, 9], [-11, 3, 8], [-11, 4, 7], [-11, 5, 6], [-10, -4, 14], [-10, -3, 13], [-10, -2, 12], [-10, -1, 11], [-10, 0, 10], [-10, 1, 9], [-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, -5, 14], [-9, -4, 13], [-9, -3, 12], [-9, -2, 11], [-9, -1, 10], [-9, 0, 9], [-9, 1, 8], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -6, 14], [-8, -5, 13], [-8, -4, 12], [-8, -3, 11], [-8, -2, 10], [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-8, 4, 4], [-7, -7, 14], [-7, -6, 13], [-7, -5, 12], [-7, -4, 11], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4], [-6, -6, 12], [-6, -5, 11], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, -1, 7], [-6, 0, 6], [-6, 1, 5], [-6, 2, 4], [-6, 3, 3], [-5, -5, 10], [-5, -4, 9], [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1]]

# print len(solution.threeSum(test))
# for t in solution.threeSum(test):
#     if t not in test1:
#         print t

print solution.threeSum(test)
