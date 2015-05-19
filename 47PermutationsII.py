#Init self.res = []
#Append to res list when satisfies
#TLE Error
import math
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.hash_table = {}

    def _permute(self,num,determined):
        if not num :#and (determined not in self.res):
            self.res.append(determined)
        for i in range(len(num)):
            new_list = list(determined)
            new_list.append(num[i])
            #if str(new_list) not in self.hash_table:
                #self.hash_table[str(new_list)] = 1
            self._permute(num[:i]+num[i+1:], new_list)

    def permuteUnique(self, num):
        num.sort()
        self._permute(num,[])
        repeat = 1
        cur_num = num[0]
        cur_multi = 1

        self.res.sort()
        for i in range(1,len(num)):
            if cur_num == num[i]:
                cur_multi += 1
            else:
                repeat *= math.factorial(cur_multi)
                cur_multi = 1
                cur_num = num[i]
        repeat *= math.factorial(cur_multi)
        #print num, repeat
        res = []
        for i in range(len(self.res)/repeat):
            res.append(self.res[i*repeat])
        self.res = res
        return self.res

#Trying compare string
#Damn! TLE again!
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.last = []

    def _permute(self,num,determined):
        if not num and determined > self.last:
            self.res.append(determined)
            self.last = determined
        for i in range(len(num)):
            new_list = list(determined)
            new_list.append(num[i])
            self._permute(num[:i]+num[i+1:], new_list)

    def permuteUnique(self, num):
        num.sort()
        self._permute(num,[])
        return self.res


#Trying start pos
#Wrong! [[0, 0, 2, 3], [0, 0, 3], [0, 2, 3], [0, 3], [0, 2, 3], [0, 3], [2, 3], [3]] for [0,0,2,3]
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []

    def _permute(self, num, start, determined):
        if start == len(num):
            self.res.append(determined)
        for i in range(start, len(num)):
            new_list = list(determined)
            new_list.append(num[i])
            self._permute(num, i+1, new_list)

    def permuteUnique(self, num):
        num.sort()
        self._permute(num,0,[])
        return self.res


#Trying increasing order in each element
#[[0, 0, 2, 3]] ...
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.last = -1

    def _permute(self, num, last, determined):
        if not num:
            self.res.append(determined)
            self.last = last
        for i in range(len(num)):
            if num[i] > self.last:
                new_list = list(determined)
                new_list.append(num[i])
                self._permute(num[:i]+num[i+1:], num[i], new_list)

    def permuteUnique(self, num):
        num.sort()
        self._permute(num, self.last, [])
        return self.res




#Trying to do with dictionary
#Wrong, without return...... WHY?
# ([3,0,0,2]) = 36
# 1 depth   1 {1: 1, 2: 1} []
# 2 depth   1 {1: 0, 2: 1} [1]
# 2 depth   2 {1: 0, 2: 1} [1]
# [1, 2]
# 3 depth   1 {1: 0, 2: 0} [1, 2]  -> Extra 1 depth, which should not exist, make len(key) numbers of res
#See below OK now
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.hash_table = {}

    def _permute(self, num, determined, depth):
        depth += 1
        #OK now
        #Extra 1 depth, which should not exist, make different len(key) times of res
        for key in self.hash_table:
            if len(determined) == len(num):
                self.res.append(determined)
                print determined
                #Wrong, without return...... WHY?
                # ([3,0,0,2]) = 36
                #return
            print  depth,'depth  ', key, self.hash_table, determined
            if self.hash_table[key] > 0:

                self.hash_table[key] -= 1

                new_list = list(determined)
                new_list.append(key)

                self._permute(num, new_list, depth)
                self.hash_table[key] += 1
        depth -= 1

    def permuteUnique(self, num):
        for n in num:
            if n in self.hash_table:
                self.hash_table[n] += 1
            else:
                self.hash_table[n] = 1
        #print self.hash_table
        self._permute(num, [], 0)
        return self.res




# 1 {1: 1, 2: 1} []
# 1 {1: 0, 2: 1} [1]
# 2 {1: 0, 2: 1} [1]
# [1, 2]
# 2 {1: 1, 2: 1} []
# 1 {1: 1, 2: 0} [2]
# [2, 1]
# 2 {1: 1, 2: 0} [2]
# [[1, 2], [2, 1]]

# 1 depth   1 {1: 1, 2: 1} []
# 2 depth   1 {1: 0, 2: 1} [1]
# 2 depth   2 {1: 0, 2: 1} [1]
# [1, 2]
# 3 depth   1 {1: 0, 2: 0} [1, 2]  -> Extra 1 depth, which should not exist, make different len(key)  times of res
# [1, 2]                              for key in self.hash_table:  Right here
# 3 depth   2 {1: 0, 2: 0} [1, 2]
# 1 depth   2 {1: 1, 2: 1} []
# 2 depth   1 {1: 1, 2: 0} [2]
# [2, 1]
# 3 depth   1 {1: 0, 2: 0} [2, 1]
# [2, 1]
# 3 depth   2 {1: 0, 2: 0} [2, 1]
# 2 depth   2 {1: 1, 2: 0} [2]
# [[1, 2], [1, 2], [2, 1], [2, 1]]


##########################
#Using hash table (dictionary), Avoiding using repeated elements
#Trying to do with dictionary
#This is good. WHY?
#This is the correct answer
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.hash_table = {}

    def _permute(self, num, determined, depth):
        for key in self.hash_table:
            depth += 1
            if len(determined) == len(num):
                self.res.append(determined)
                print determined
                return
            print depth, 'depth  ', key, self.hash_table, determined
            if self.hash_table[key] > 0:

                self.hash_table[key] -= 1

                new_list = list(determined)
                new_list.append(key)

                self._permute(num, new_list, depth)
                self.hash_table[key] += 1
            depth -= 1

    def permuteUnique(self, num):
        for n in num:
            if n in self.hash_table:
                self.hash_table[n] += 1
            else:
                self.hash_table[n] = 1
        print self.hash_table
        self._permute(num, [], 0)
        return self.res


#Init self.res = []
#Append to res list when satisfies
#This is list based, duplicated results
#See sorted list method
# class Solution:
#     # @param num, a list of integer
#     # @return a list of lists of integers
#     def __init__(self):
#         self.res = []
#
#     def _permute(self,num,determined, depth):
#         depth += 1
#         if not num:
#             self.res.append(determined)
#             return
#         print depth, 'depth  ', determined
#         print 'res  ', self.res
#         for i in range(len(num)):
#             new_list = list(determined)
#             new_list.append(num[i])
#             self._permute(num[:i]+num[i+1:], new_list, depth)
#         depth -= 1
#
#     def permuteUnique(self, num):
#         self._permute(num,[],0)
#         return self.res
#
# solution = Solution()
# res = solution.permuteUnique([1,1,2])
# print res

#Testing speed with different size of parameters in the stack for the recursion
class Solution:
    @staticmethod
    def _permuteUnique(res, hash_table, length, determined):
        if len(determined) == length:
            res.append(determined)
            return
        for key in hash_table.keys():
            if hash_table[key] > 0:
                new_list = list(determined)
                new_list.append(key)
                hash_table[key] -= 1
                Solution._permuteUnique(res, hash_table, length, new_list)
                hash_table[key] += 1

    def permuteUnique(self, num):
        res = []
        length = len(num)
        hash_table = {}
        for i in range(length):
            if num[i] in hash_table:
                hash_table[num[i]] += 1
            else:
                hash_table[num[i]] = 1
        Solution._permuteUnique(res, hash_table, length,[])
        return res
solution = Solution()
print len(solution.permuteUnique([1,1,0,0,1,-1,-1,1]))

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        numPool = {}
        for i in num:
            if i in numPool:
                numPool[i] += 1
            else:
                numPool[i] = 1
        return self.dfs(numPool, [[]])

    def dfs(self, numDic, filled):
        returned_list = []
        for eachkey in numDic:
            if numDic[eachkey] > 0:
                pass_list = [x + [eachkey] for x in filled]
                numDic[eachkey] -= 1
                extended_lists = self.dfs(numDic,pass_list)
                numDic[eachkey] += 1
                returned_list.extend(extended_lists)
        return returned_list if len(returned_list) > 0 else filled




##########################
#Using Sorted list, Avoiding using repeated elements
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []
        num.sort()
        return self.permute(num)

    def permute(self, num):
        if len(num) == 1:
            return [num]
        ret = []
        prev = None
        for i in range(len(num)):
            if prev != num[i]:
                prev = num[i]
                for elt in self.permute(num[:i]+num[i+1:]):
                    ret.append([num[i]]+elt)
        return ret

##########################
#Avoiding using Sorted list, Using dictionary (with extra space of copy of dictionaries)
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []
        hash_table = {}
        for i in range(len(num)):
            if num[i] not in hash_table:
                hash_table[num[i]] = 1
        return self.permute(num, hash_table)

    def permute(self, num, hash_table):
        if len(num) == 1:
            return [num]
        ret = []
        hash_copy = dict(hash_table)
        for i in range(len(num)):
            if num[i] in hash_copy:
                hash_copy.pop(num[i])
                for elt in self.permute(num[:i]+num[i+1:], hash_table):
                    ret.append([num[i]]+elt)
        return ret

    # def _permute(self, num, determined, depth):
    #     for key in self.hash_table:
    #         depth += 1
    #         if len(determined) == len(num):
    #             self.res.append(determined)
    #             print determined
    #             return
    #         print depth, 'depth  ', key, self.hash_table, determined
    #         if self.hash_table[key] > 0:
    #
    #             self.hash_table[key] -= 1
    #
    #             new_list = list(determined)
    #             new_list.append(key)
    #
    #             self._permute(num,new_list, depth)
    #             self.hash_table[key] += 1
    #         depth -= 1


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []
        num.sort()
        return self.permute(num)

    def permute(self, num):
        if len(num) == 1:
            return [num]
        ret = []
        prev = None
        for i in range(len(num)):
            if prev != num[i]:
                prev = num[i]
                for elt in self.permute(num[:i]+num[i+1:]):
                    ret.append([num[i]]+elt)
        print id(ret)
        return ret


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.hash_table = {}

    def _permute(self, num, determined):
        for key in self.hash_table:
            if len(determined) == len(num):
                self.res.append(determined)
                return
            if self.hash_table[key] > 0:
                self.hash_table[key] -= 1
                # new_list = list(determined)
                # new_list.append(key)
                #new_list = [x for x in determined + [key]]
                self._permute(num, [x for x in determined + [key]])
                self.hash_table[key] += 1

    def permuteUnique(self, num):
        for n in num:
            if n in self.hash_table:
                self.hash_table[n] += 1
            else:
                self.hash_table[n] = 1
        self._permute(num, [])
        return self.res

solution = Solution()
print solution.permuteUnique([1,2,3])
# dict = {1:0,2:0}
# d = dict
# d[1] =1
# print dict
# ->It is true that the parameters are reference, however, it does not mean the stack will not overflow (Not the number of the reference).
#  1)If we pass immutable objects(like string), we will definitely need more space since when we assign a new value to the parameter new objects
#  are created and maintained. 2)If we are passing mutable objects(like list or dictionary), it depends on whether we are
# rebinding the reference. When we simply mutate those mutable objects(e.g. numDic here), we are not allocating new space.
# When we rebind the mutable reference(eg. filled here), we are actually making the reference point to new objects.Print out
# id(numDic) and id(filled) to check that.

# I think using a dictionary to keep check of number of the unused elements in num is the best answer fot the this problem.
# Since sorting does need extra time and using num[:i]+num[i+1:] does need extra space.
#
#
# "for i in range(len(num)): if num[i] not in hashtable: hashtable[num[i]] = 1 " I don't understand how do you count the duplicates?
# ->It is the same logic with the second solution with prev, the solution is placing numbers in one position at each step, hashtable is keeping track of whether the same number is already placed in the current position.
# "the only copy of the object is in the permuteUnique(), and all the others are merely references."
# ->It is true that the parameters are reference, however, it does not mean the stack will not overflow (Not the number of the reference).
#  1)If we pass immutable objects(like string), we will definitely need more space since when we assign a new value to the parameter new objects are created and maintained.
# 2)If we are passing mutable objects(like list or dictionary), it depends on whether we are rebinding the reference. When we simply mutate those mutable objects(e.g. numDic here), we are not allocating new space.When we rebind the mutable reference(eg. filled here), we are actually making the reference point to new objects.Print out id(numDic) and id(filled) to check that.
# I think using a dictionary to keep check of number of the unused elements in num is the best answer for the this problem. Since sorting does need extra time and using num[:i]+num[i+1:] does need extra space.


# determined = [1,2]
#
# new_list = [x for x in determined + [3]]
# print new_list