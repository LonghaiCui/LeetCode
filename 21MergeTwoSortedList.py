# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        temp = ListNode(0)
        head = temp

        while l1 and l2:
            if l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next

        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return head.next

ListNode1 = ListNode(1)
ListNode2 = ListNode(2)
ListNode3 = ListNode(3)
ListNode4 = ListNode(4)
ListNode1.next = ListNode2
ListNode2.next = ListNode3
ListNode3.next = ListNode4

ListNodea = ListNode(3.4)


ListNode1.next = ListNode2
ListNode2.next = ListNode3

solution = Solution()
head= solution.mergeTwoLists(ListNode1,ListNodea)
while head:
    print head.val
    head = head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Google O(n)
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        temp = dummyHead = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1

        if l2:
            temp.next = l2

        return dummyHead.next
#Recursive
def mergeTwoLists(self, l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    else:
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
