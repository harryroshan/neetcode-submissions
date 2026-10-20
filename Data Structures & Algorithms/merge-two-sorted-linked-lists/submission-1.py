# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node_list1 = list1
        current_node_list2 = list2
        current_node_combined_list = None
        combined_list_head = None
        while current_node_list1 is not None and current_node_list2 is not None:
            if current_node_list1.val < current_node_list2.val:
                target_node = current_node_list1
                current_node_list1 = current_node_list1.next
            else:
                target_node = current_node_list2
                current_node_list2 = current_node_list2.next
            if combined_list_head is None:
                combined_list_head = target_node
                current_node_combined_list = target_node
            else:
                current_node_combined_list.next = target_node
                current_node_combined_list = target_node
        if current_node_list1 is not None:
            if combined_list_head is None:
                return current_node_list1
            else:
                current_node_combined_list.next = current_node_list1
        if current_node_list2 is not None:
            if combined_list_head is None:
                return current_node_list2
            else:
                current_node_combined_list.next = current_node_list2
        return combined_list_head