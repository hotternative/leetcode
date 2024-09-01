from typing import Optional
from utils.linked_list_utils import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while True:
            if not head.next:
                return False
            if hasattr(head, "visited"):
                return True
            head.visited = True
            head = head.next
