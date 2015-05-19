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

# class Solution:
#     # @param {ListNode} head
#     # @param {integer} x
#     # @return {ListNode}
#     def partition(self, head, x):
#         node = head
#         prev = ListNode(0,-1)
#         prev.next = head
#         head = prev
#         start, end = None, None
#         while node:
#             if node.val >= x:
#                 if not start:
#                     start, end = node, node
#                 print start.id, end.id
#                 while node.next:
#                     node = node.next
#                     if node.val < x:
#                         break
#                     end = node
#                 #print 'node', node.id
#                 print 'start, end, node, prev', start.id, end.id, node.id, prev.id
#                 if node.next:
#                     print 'kkk'
#                     end.next = node.next #3 -> None
#                     node.next = start #None.next =
#                     prev.next = node
#                     node = end
#                 else:
#                     print 'xxx'
#                     node.next = start
#                     prev.next = node
#                     end.next = None
#                     return head.next
#                     #node = end.next
#                     #
#
#             prev = prev.next
#                 #prev.next = node
#             #prev.next = node
#
#
#             node = node.next
#             print_nodes(head.next)
#             # if node:
#             #     print node.id, node.val
#             #print node.val
#             # if not node:
#             #     return head.next
#
#             # if not node:
#             #     return head.next
#
#
#
#         #return head.next
#
#
#
#
#
#
#

#
# class ListNode:
#     def __init__(self, x, id):
#         self.val = x
#         self.next = None
#         self.id = id
#
# class Solution:
#     # @param {ListNode} head
#     # @param {integer} x
#     # @return {ListNode}
#     def partition(self, head, x):
#         node = head
#         prev = ListNode(0,-1)
#         prev.next = head
#         head = prev
#         start, end = None, None
#         while node:
#             if node.val >= x:
#                 if not start:
#                     start, end = node, node
#                 print start.id, end.id
#                 while node.next:
#                     node = node.next
#                     if node.val < x:
#                         break
#                     end = node
#                 #print 'node', node.id
#                 print 'start, end, node, prev', start.id, end.id, node.id, prev.id
#                 if node.next:
#                     print 'kkk'
#                     end.next = node.next #3 -> None
#                     node.next = start #None.next =
#                     prev.next = node
#                     node = end
#                 else:
#                     print 'xxx'
#                     node.next = start
#                     prev.next = node
#                     end.next = None
#                     return head.next
#                     #node = end.next
#                     #
#
#             prev = end
#                 #prev.next = node
#             #prev.next = node
#
#
#             node = node.next
#             print_nodes(head.next)
#             # if node:
#             #     print node.id, node.val
#             #print node.val
#             # if not node:
#             #     return head.next
#
#             # if not node:
#             #     return head.next
#
#
#
#         #return head.next
# class Solution:
#     # @param {ListNode} head
#     # @param {integer} x
#     # @return {ListNode}
#     def partition(self, head, x):
#         node = head
#
#         prev = ListNode(0,-1)
#         prev.next = head
#         head = prev
#
#         last = None
#
#         while node:
#             print 'Node.val', node.val
#             if node.val < x:
#                 print ' node.val, prev.val, ', node.val, prev.val
#                 if last:
#                     print 'last' , last.val
#                 if not last:
#                     last = node
#                     node = node.next
#                     prev = prev.next
#                     continue
#
#                 node.next = last.next
#                 last.next = node
#                 last = last.next
#
#             node = node.next
#             prev = prev.next
#             print_nodes(head.next)
#
#         return head.next



# class Solution:
#     # @param {ListNode} head
#     # @param {integer} x
#     # @return {ListNode}
#     def partition(self, head, x):
#         #Mark current node
#         current = head
#         #Mark previous node
#         prev = ListNode(-1,-1)
#         prev.next = head
#         #Mark last node that is smaller than x
#         last = None
#         #Mark prev in order to return head (return head.next)
#         head = prev
#
#         while current:
#             print current.val
#             if current.val >= x:
#                 print 'a'
#                 current = current.next
#                 prev = prev.next
#             else:
#                 if not last:
#                     last = current
#                     prev = prev.next
#                     current = current.next
#                     continue
#                 # if prev == last:
#                 #     print 'b'
#                 #     current = current.next
#                 #     prev = prev.next
#                 #     last = last.next
#                 #
#                 # else:
#                 print 'c'
#                 prev.next = current.next
#                 current.next = last.next
#                 last.next = current
#
#                 last = last.next
#                 current = prev.next
#
#         return head.next


class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        #Mark current node
        current = head
        #Mark previous node
        prev = ListNode(-1,-1)
        prev.next = head
        #Mark last node that is smaller than x
        last = prev
        #Mark prev in order to return head (return head.next)
        head = prev

        while current:
            print current.val
            if current.val >= x:
                print 'a'
                current = current.next
                prev = prev.next
            else:
                # if not last:
                #     last = current
                #     prev = prev.next
                #     current = current.next
                #     continue
                if prev == last:
                    print 'b'
                    current = current.next
                    prev = prev.next
                    last = last.next

                else:
                    print 'c'
                    prev.next = current.next
                    current.next = last.next
                    last.next = current

                    last = last.next
                    current = prev.next

        return head.next

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        current = last = ListNode(-1,-1)
        current.next = head
        last = head
        while current.next:
            if current.next.val >= x:
                current = current.next
            else:
                if current == last:
                    current = last = current.next
                    #Move last, prev and current forward

                else:
                    #Put the current node between last and last.next
                    current.next = current.next.next
                    current.next.next = last.next
                    last.next = current.next
                    #Update node last and current, node prev remains the same
                    last = current.next

        return head



#->1->4->3->2->5->1->2
l1 = ListNode(5,0)
l2 =ListNode(1,1)
l3 =ListNode(3,2)
l4 =ListNode(2,3)
l5 =ListNode(4,4)
l6 =ListNode(5,5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

print_nodes(l1)
solution = Solution()
ret = solution.partition(l1, 3)
print_nodes(ret)



#->1->4->3->2->5->1->2
# l1 = ListNode(1,0)
# l2 =ListNode(4,1)
# l3 =ListNode(3,2)
# l4 =ListNode(2,3)
# l5 =ListNode(5,4)
# l6 =ListNode(0.5,5)
# l7 =ListNode(0.6,6)
# l8 =ListNode(4,7)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
# l6.next = l7
# #l7.next = l8
# print_nodes(l1)
# solution = Solution()
# ret = solution.partition(l1, 3)
# print_nodes(ret)
#
#
#
# l1 = ListNode(3,0)
# l2 =ListNode(3,1)
# l3 =ListNode(1,2)
# l4 =ListNode(2,3)
# l5 =ListNode(4,4)
#
# l6 =ListNode(3,5)
# l7 =ListNode(2,6)
# l8 =ListNode(4,7)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# # l5.next = l6
# l6.next = l7
# #l7.next = l8
#
#
# [3,3,1,2,4], 3
