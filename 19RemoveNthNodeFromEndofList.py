# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        length = 0
        values = []
        cur_node = head
        while cur_node is not None:
            values.append(cur_node.val)
            cur_node = cur_node.next
            length += 1

        #Only 1 node in the list, return None
        if length == 1:
            return None
        #if remove the first element, return head.next
        if n == length:
            return head.next

        cur_node = head
        cur_pos = 0

        while cur_pos < length - n - 1:
            cur_node = cur_node.next
            cur_pos += 1
        cur_node.next = cur_node.next.next
        return head

ListNode1 = ListNode(1)
ListNode2 = ListNode(2)
ListNode3 = ListNode(3)
ListNode4 = ListNode(4)
ListNode1.next = ListNode2
#ListNode2.next = ListNode3
#ListNode3.next = ListNode4

solution = Solution()
node = solution.removeNthFromEnd(ListNode1, 2)
while node is not None:
    print node.val
    node = node.next