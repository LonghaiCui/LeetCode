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
    def _reverseList(self, head, x):
        print x
        if not head:
            return
        if not head.next:
            return head


        current = head
        p1 = current.next
        p2 = p1.next

        if not p2:
            p1.next = head
            head.next = None
            return p1

        for i in range(x):
            p1.next = current
            current = p1
            p1 = p2
            p2 = p2.next

            if not p2:
                p1.next = current
                head.next = None
                return p1


        p1.next = current
        head.next = p2

        return p1

    def reverseList(self, head, m, n):
        if m == n:
            return head
        #Reverse from head
        if m == 1:
            return self._reverseList(head, n - 2)


        prev = head
        for i in range(m - 2):
            prev = prev.next

        current = prev.next

        prev.next = self._reverseList(current, n - m - 1)
        return head


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
#l2.next = l3
#l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
#l7.next = l8
print_nodes(l1)
solution = Solution()
ret = solution.reverseList(l1,1,2)
print_nodes(ret)