__author__ = 'longhaicui'


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_table = {}
        for i in range(len(num)):
            if target - num[i] not in hash_table:
                hash_table[num[i]] = i + 1
            else:
                return hash_table[target - num[i]], i + 1
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        print nums
        ret = set()
        for i in range(len(nums)-3):
            p1 = i
            for j in range(i+1, len(nums)-2):
                p2 = j
                p3 = j+1
                p4 = len(nums)-1
                #print p1, p2, p3, p4
                #Using cur_target to avoid duplicated computation
                cur_target = target - nums[p1] - nums[p2]
                while p3 < p4:
                    if nums[p3] + nums[p4] == cur_target:
                        print type ((nums[p1],nums[p2],nums[p3],nums[p4]))
                        ret.add((nums[p1],nums[p2],nums[p3],nums[p4]))
                        p3 += 1
                        continue
                    if nums[p3] + nums[p4] > cur_target:
                        p4 -= 1
                    else:
                        p3 += 1
        return [list(x) for x in list(ret)]

import collections
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = set()
        cache = {}
        for b in xrange(1, len(nums) - 2):
            for a in xrange(b):
                if nums[a] + nums[b] not in cache:
                    cache[nums[a] + nums[b]] = set()
                cache[nums[a] + nums[b]].add((nums[a], nums[b]))
            c = b + 1
            for d in xrange(c + 1, len(nums)):
                remainder = target - nums[c] - nums[d]
                if remainder in cache:
                    for half in cache[remainder]:
                       result.add(tuple(list(half) + [nums[c], nums[d]]))
        return [list(x) for x in list(result)]
        return map(list, result)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4 or target is None:
            return []
        nums.sort()
        cache = {}
        ret = set()
        for b in xrange(1, len(nums)-2):

            for a in xrange(b):
                remained = target - nums[a] - nums[b]
                if remained not in cache:
                    cache[remained] = set()
                cache[remained].add((nums[a], nums[b]))

            c = b + 1
            for d in xrange(c+1, len(nums)):
                cur_value = nums[c] + nums[d]
                if cur_value in cache:
                    for half in cache[cur_value]:
                        ret.add(tuple(list(half)+[nums[c],nums[d]]))

        return map(list,ret)

solution = Solution()
print solution.fourSum([1, 0, -1, 0, -2, 2], 0)
#print solution.fourSum([91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245], -236727523)

#Brute force
#Time n2 Space 1

# class Solution:
#     # @return a tuple, (index1, index2)
#     def twoSum(self, num, target):
#         # return -1, -1
#         n = len(num)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if num[i] + num[j] == target:
#                     #print num[i], num[j],target
#                     #print "index1 = %d, index2 = %d" % (i+1, j+1)
#                     return i+1, j+1


# Hash table
#Time n space n

# class Solution:
#     # @return a tuple, (index1, index2)
#     # 8:42
#     def twoSum(self, num, target):
#         map = {}
#         for i in range(len(num)):
#             if num[i] not in map.keys():
#                 map[target - num[i]] = i + 1
#             else:
#                 return map[num[i]], i + 1
#
#         return -1, -1
#
