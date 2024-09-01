from utils.linked_list_utils import ListNode
from typing import Optional

class Solution:
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1


        if list1.val < list2.val:
            head = list1
            head.next = Solution.mergeTwoLists(list1.next, list2)
        else:
            head = list2
            head.next = Solution.mergeTwoLists(list1, list2.next)
        return head

# I also need to practice on an iterative solution
class Solution_Iterative:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        cur = head

        while list1 and list2:

            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        if not list1:
            cur.next = list2

        if not list2:
            cur.next = list1

        return head