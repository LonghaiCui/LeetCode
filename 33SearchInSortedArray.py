class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1
        if nums[0] < nums[-1]:
            #print 'here'
            start_index = 0
        else:
            start = 0
            end = len(nums)-1
            mid = (start + end)/2
            print start, mid, end
            if nums[mid] < nums[end]:
                start_index = mid
            else:
                while nums[mid] > nums[end]:
                    if nums[mid] > nums[start]:
                        start = mid + 1
                    else:
                        end = mid - 1
                    mid = (start + end)/2
                    print start, mid, end


                start_index = start if mid!= -1 else len(nums)-1


        print 'start_index', start_index
        if target > nums[start_index-1] or target < nums[start_index]:
            return -1
        if target > nums[len(nums)-1]:
            start = 0
            end = start_index - 1
        else:
            start = start_index
            end = len(nums)-1
        mid = (start+end)/2
        while start <= end:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)/2
        return -1


class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        #start != end
        while start < end:

            mid = (start + end) / 2

            if target == nums[mid]:
                return mid

            #mid != start
            if mid == start and nums[mid] != target:
                return -1

            if nums[start] > nums[end]:
                if nums[mid] > nums[start]:
                    if nums[start] < target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else: #mid != start
                    if nums[mid] < target < nums[end]: # mid == end?
                        start = mid + 1
                    else:
                        end = mid - 1

            else: #start != end
                if target < nums[start] or target > nums[end]:
                    return -1
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        #start != end
        while start < end:

            mid = (start + end) / 2
            #print 'before', start, mid, end
            if nums[start] == target:
                return start
            if nums[mid] == target:
                return mid
            if nums[end] == target:
                return end


            if nums[start] > nums[end]:
                #print 'mid, start', nums[mid], nums[start]
                if nums[mid] > nums[start]:
                    #print 'mid > start'
                    if nums[start] < target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else: #mid != start
                    if nums[mid] < target < nums[end]: # mid == end?
                        start = mid + 1
                    else:
                        end = mid - 1

            else: #start != end

                if target < nums[start] or target > nums[end]:
                    return -1
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

            #print 'after', start, mid, end

        if start == end and target == nums[start]:
            return start

        return -1


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            # if nums[start] == target:
            #     return start
            if nums[mid] == target:
                return mid
            # if nums[end] == target:
            #     return end

            if nums[start] >= nums[end]:
                #print mid, start
                if mid == start and nums[start] == target:
                    return start
                if nums[mid] >= nums[start]:
                    if nums[start] <= target <= nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if nums[mid] <= target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
            else:

                if target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            # if nums[start] <= nums[end]:
            #     if target >= nums[mid]:
            #         start = mid + 1
            #     else:
            #         end = mid - 1
            # else:
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

solution = Solution()
print solution.search([1],1)
print solution.search([1,3,5], 1)

print solution.search([3,1], 1)
print solution.search([4,5,6,0,1,2], 0)
print solution.search([4,5,6,7,0,1,2], 0)

print solution.search([5,1,3], 1)
print solution.search([7,8,1,2,3,4,5,6], 1)

class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1



