class Solution:
    def _search(self, nums, target, start, end, d):

        while start <= end:
            copy_start = start
            copy_end = end
            mid = (start + end) / 2
            print 'while', start,mid, end


            if nums[mid] == target:
                return True

            if start == mid:
                return False




            if nums[mid] > nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            elif nums[mid] < nums[start]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

            elif nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

            elif nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1


            if nums[mid] == nums[start]:
                new_start = start + 1
                new_end = mid - 1
                print new_start, new_end
                depth = d + 1
                flag = self._search(nums, target, new_start, new_end, depth)

                print 'here'
                if flag:
                    return True

            if nums[mid] == nums[end]:
                new_start = mid + 1
                new_end = end - 1
                depth = d + 1
                print new_start, new_end
                flag = self._search(nums, target, new_start, new_end, depth)

                print '1here'
                if flag:
                    return True

                print '1there'
            if copy_start == start and copy_end == end:
                return False
            print 'Go to next loop'




        return False

    def search(self, nums, target):
        if not nums:
            return False
        # if len(nums) == 1:
        #     return True if nums[0] == target else False
        start, end = 0, len(nums) - 1

        return self._search(nums, target, start, end, 0)


#First Acceptance
class Solution:
    def _search(self, nums, target, start, end):

        while start <= end:
            copy_start = start
            copy_end = end
            mid = (start + end) / 2

            if nums[mid] == target:
                return True

            if nums[mid] > nums[start] or nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            elif nums[mid] < nums[start] or nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

            # elif nums[mid] < nums[end]:
            #     if nums[mid] <= target <= nums[end]:
            #         start = mid + 1
            #     else:
            #         end = mid - 1
            #
            # elif nums[mid] > nums[end]:
            #     if nums[start] <= target <= nums[mid]:
            #         end = mid - 1
            #     else:
            #         start = mid + 1

            if nums[mid] == nums[start]:
                if self._search(nums, target, start + 1, mid- 1):
                    return True

            if nums[mid] == nums[end]:
                if self._search(nums, target, mid + 1, end - 1):
                    return True


            if copy_start == start and copy_end == end:
                return False

        return False

    def search(self, nums, target):
        if not nums:
            return False
        start, end = 0, len(nums) - 1
        return self._search(nums, target, start, end)

#As long as we know the largest number is on left half or right half for each loop, it is the same with the original problem,
#which is to search number from rotated sorted array without duplicates.

#The key is to decide the largest element is in which half of the current range for each loop.It is a little bit hard to
#that with duplicated elements in the input list in the list like 11121, where elements in the start, middle and end
# positions are equal. So what we can do is 1) For those cases where we can know which half the largest element is located,
#reduce the range by changing start or end position. 2) For those cases where we can not decide, we recursively search for both sides.

solution = Solution()
print solution.search([1,1,1,2,3,1],4)