from utils.linked_list_utils import (
    create_singly_linked_list_from_list_of_values,
    create_list_of_values_from_singly_linked_list,
    ListNode
)
import unittest
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        next = head.next
        head.next = None

        while True:
            if not next:
                return head

            next_next: ListNode | None = next.next
            next.next = head
            head = next
            next = next_next



class TestSolution(unittest.TestCase):

    def test1(self):
        head = [1, 2]

        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        new_head_node = sol.reverseList(head_node)
        actual_output = create_list_of_values_from_singly_linked_list(new_head_node)
        print(actual_output)

