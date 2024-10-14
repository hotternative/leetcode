# Runtime 770 ms Beats 96.41% Memory 46.8 MB Beats 38.23%
from typing import Optional
from utils.linked_list_utils import ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = [head.val]
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            l.append(cur_node.val)

        i, j = 0, len(l) - 1
        while i <= j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1

        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]