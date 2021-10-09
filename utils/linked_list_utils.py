def create_singly_linked_list_from_list_of_values(list_of_values):
    head_node = cur_node = ListNode(val=list_of_values[0])
    for node_val in list_of_values[1:]:
        new_node = ListNode(val=node_val)
        cur_node.next = new_node
        cur_node = new_node
    return head_node


def create_list_of_values_from_singly_linked_list(head):
    list_of_values = []
    while head:
        list_of_values.append(head.val)
        head = head.next
    return list_of_values


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next