# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# Definition for singly-linked list.
from typing import Optional
import unittest

from utils.linked_list_utils import (
    create_singly_linked_list_from_list_of_values,
    create_list_of_values_from_singly_linked_list,
    ListNode
)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 24 ms, faster than 96.73%, Memory Usage: 14.2 MB, less than 71.70%
        """
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
        return slow

class TestSolution(unittest.TestCase):

    def test1(self):
        head = [1,2,3,4,5]
        expected_output = [3,4,5]
        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        middle_node = sol.middleNode(head_node)
        actual_output = create_list_of_values_from_singly_linked_list(middle_node)
        assert expected_output == actual_output

    def test2(self):
        head = [1,2,3,4,5,6]
        expected_output = [4,5,6]
        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        middle_node = sol.middleNode(head_node)
        actual_output = create_list_of_values_from_singly_linked_list(middle_node)
        assert expected_output == actual_output