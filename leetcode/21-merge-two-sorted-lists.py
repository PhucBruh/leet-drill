from leetcode.list_node import ListNode


# greedy choice approach
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        head = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        dummy.next = list1 or list2
        return head.next


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
result = solution.mergeTwoLists(l1, l2)
print(result.val)
