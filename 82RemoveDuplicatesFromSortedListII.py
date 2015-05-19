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

        prev = ListNode(0,-1)
        prev.next = head
        head = prev

        while node.next:
            flag = False
            while node.next and node.val == node.next.val:
                node.next = node.next.next
                flag = True
            node = node.next
            if flag and prev.next:
                prev.next = prev.next.next
            else:
                #node = node.next
                prev = prev.next
            if not node:
                return head.next
        return head.next


def print_nodes(l):
    s = ''
    while l:
        s += '->' + str(l.val)
        l = l.next
    print s


l1 = ListNode(1,0)
l2 =ListNode(1,1)
l3 =ListNode(2,2)
l4 =ListNode(2,3)

l5 =ListNode(2,4)
l6 =ListNode(3,5)
l7 =ListNode(3,6)
l8 =ListNode(4,7)

l1.next = l2
#l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
solution = Solution()
print_nodes(solution.deleteDuplicates(l1))

#print_nodes(l)

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        node = head
        prev = ListNode(0)
        prev.next = head
        head = prev

        while node:
            #Check if current node is a duplicated node
            flag = False
            while node.next and node.val == node.next.val:
                node.next = node.next.next
                flag = True
            #Node is now pointer of a list with each element appears only once
            node = node.next
            #Delete the current node if its value appeared more than once
            if flag and prev.next:
                prev.next = prev.next.next
            #Put the node at the end of the result
            else:
                prev = prev.next

        return head.next