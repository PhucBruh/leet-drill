# Definition for singly-linked list.
from ast import dump


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Fast - Slow approach
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


# Hash approach - the same way with Stack/Queue
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: Optional[ListNode]
#         :type n: int
#         :rtype: Optional[ListNode]
#         """
#
#         curr = head
#         count = 1
#         h = {}
#         h[1] = curr
#
#         while curr.next:
#             count += 1
#             curr = curr.next
#             h[count] = curr
#
#         target = count - n + 1
#         if target == 1:
#             return head.next
#
#         prev = h[target - 1]
#
#         prev.next = prev.next.next
#
#         return h[1]


mock = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
result = solution.removeNthFromEnd(mock, 2)
