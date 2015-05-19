# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return
        length = 0
        current = head
        while current:
            length += 1
            #current will point at the last node of initial list
            if current.next is None:
                break
            current = current.next

        k %= length
        if k == 0:
            return head

        current.next = head
        for i in range(length - k):
            #current will point at the last node of desired list
            current = current.next

        head = current.next
        current.next = None
        return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
solution = Solution()
l = solution.rotateRight(l1, 6)

while l:
    print l.val
    l = l.next
