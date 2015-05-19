#Definition for singly-linked list.
class ListNode:
    def __init__(self, x, id):
        self.val = x
        self.next = None
        self.id = id

def print_nodes(l):
    s = ''
    for i in range(10):
        s += '->' + str(l.val)
        l = l.next
        if not l:
            print s
            return
    print s

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head
        current = head
        p1 = current.next
        p2 = p1.next
        current.next = None
        while p2:
            p1.next = current
            current = p1
            p1 = p2
            p2 = p2.next
        p1.next = current
        return p1


#->1->4->3->2->5->1->2
l1 = ListNode(1,0)
l2 =ListNode(4,1)
l3 =ListNode(3,2)
l4 =ListNode(2,3)
l5 =ListNode(5,4)
l6 =ListNode(0.5,5)
l7 =ListNode(0.6,6)
l8 =ListNode(4,7)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
#l7.next = l8
print_nodes(l1)
solution = Solution()
ret = solution.reverseList(l1)
print_nodes(ret)