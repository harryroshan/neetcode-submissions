# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node = head
        nodes_hashset = set()
        while current_node is not None:
            if current_node in nodes_hashset:
                return True
            nodes_hashset.add(current_node)
            current_node = current_node.next 
        return False