# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev_node = head
        current_node = head.next

        while current_node is not None:
            temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp

        head.next = None

        return prev_node