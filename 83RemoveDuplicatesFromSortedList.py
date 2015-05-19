#Definition for singly-linked list.
class ListNode:
    def __init__(self, x, y):
        self.val = x
        self.next = None
        self.id = y

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return
        node = head
        val = head.val
        while node.next:
            if val == node.next.val:
                node.next = node.next.next
            else:
                val = node.next.val
                node = node.next
        return head

def print_nodes(l):
    s = ''
    while l:
        s += '->' + str(l.val)
        l = l.next
    print s


l1 = ListNode(1,0)
l2 =ListNode(2,1)
l3 =ListNode(2,2)
l4 =ListNode(2,3)
l5 =ListNode(2,4)
l6 =ListNode(3,5)
l7 =ListNode(3,6)
l8 =ListNode(4,7)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
solution = Solution()
ret = solution.deleteDuplicates(l1)
print_nodes(l1)
