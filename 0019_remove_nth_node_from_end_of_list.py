# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from utils.linked_list_utils import (
    create_singly_linked_list_from_list_of_values,
    create_list_of_values_from_singly_linked_list,
    ListNode
)
from typing import Optional
import unittest

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dec 2022 Runtime 39 ms Beats 84.35% Memory 13.8 MB Beats 98.48%
        # https://www.enjoyalgorithms.com/blog/remove-nth-node-from-list-end
        c = 1
        cur_node = head
        while cur_node.next:
            c += 1
            cur_node = cur_node.next
        target = c - n

        if target == 0:
            return head.next

        c = 1
        cur_node = head
        while c < target:
            c += 1
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next

        return head



    def removeNthFromEnd_2021(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2021
        counter = 1
        static_head = head
        while head.next:
            counter += 1
            head = head.next
        target_to_remove = counter - n + 1

        if counter == 1:
            return None
        if target_to_remove == 1:
            return static_head.next

        counter = 1
        head = static_head
        while head.next:
            counter += 1
            if counter == target_to_remove:
                head.next = head.next.next
                break
            head = head.next

        return static_head



class TestSolution(unittest.TestCase):

    def test1(self):
        head = [1,2,3,4,5]
        n = 2
        expected_output = [1, 2, 3, 5]
        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        new_head_node = sol.removeNthFromEnd(head_node, n)
        actual_output = create_list_of_values_from_singly_linked_list(new_head_node)
        assert expected_output == actual_output

    def test2(self):
        head = [1]
        n = 1
        expected_output = []
        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        new_head_node = sol.removeNthFromEnd(head_node, n)
        actual_output = create_list_of_values_from_singly_linked_list(new_head_node)
        assert expected_output == actual_output

    def test3(self):
        head = [1,2]
        n = 1
        expected_output = [1]
        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        new_head_node = sol.removeNthFromEnd(head_node, n)
        actual_output = create_list_of_values_from_singly_linked_list(new_head_node)
        assert expected_output == actual_output

    def test4(self):
        head = [1,2]
        n = 2
        expected_output = [2]
        head_node = create_singly_linked_list_from_list_of_values(head)
        sol = Solution()
        new_head_node = sol.removeNthFromEnd(head_node, n)
        actual_output = create_list_of_values_from_singly_linked_list(new_head_node)
        assert expected_output == actual_output