__author__ = 'longhaicui'
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(-1)
        current_node = l3
        flag = 0
        # current_node = l2
        # while current_node is not None:
        #     print current_node.val
        #     current_node = current_node.next

        while l1 is not None and l2 is not None:
            if flag == 0:
                val = l1.val + l2.val
            else:
                val = l1.val + l2.val + 1

            if val >= 10:
                val -= 10
                flag = 1
            else:
                flag = 0
            current_node.next = ListNode(val)
            current_node = current_node.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            if flag == 0:
                val = l1.val
            else:
                val = l1.val + 1

            if val >= 10:
                val -= 10
                flag = 1
            else:
                flag = 0

            current_node.next = ListNode(val)
            current_node = current_node.next
            l1 = l1.next

        while l2 is not None:
            if flag == 0:
                val = l2.val
            else:
                val = l2.val + 1

            if val >= 10:
                val -= 10
                flag = 1
            else:
                flag = 0

            current_node.next = ListNode(val)
            current_node = current_node.next
            l2 = l2.next
        if flag == 1:
            current_node.next = ListNode(1)

        current_node = l3.next

        return current_node
        while current_node is not None:
            print current_node.val
            current_node = current_node.next



# Definition for singly-linked list.

# class Solution:
# # @return a ListNode
#     def addTwoNumbers(self, l1, l2):
#         num1 = str(l1.val)
#         num2 = str(l2.val)
#         while l1.next:
#             l1 = l1.next
#             num1 = str(l1.val) + num1
#         while l2.next:
#             l2 = l2.next
#             num2 = str(l2.val) + num2
#         num3 = list(str(int(num1) + int(num2)))
#
#         n1 = ListNode(int(num3.pop(0)))
#         n = n1
#         while num3:
#             n = ListNode(int(num3.pop(0)))
#             n.next = n1
#             n1 = n
#         return n

# 742 + 8939 = 10140
l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(7)

l11.next = l12
l12.next = l13

l21 = ListNode(8)
l22 = ListNode(9)
l23 = ListNode(3)
l24 = ListNode(9)

l21.next = l22
l22.next = l23
l23.next = l24

solution = Solution()
l3 = solution.addTwoNumbers(l11,l21)

while l3 is not None:
    print l3.val
    l3 = l3.next