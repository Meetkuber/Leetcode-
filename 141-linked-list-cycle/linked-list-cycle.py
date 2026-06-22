# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
##FLoyds tortoise and hare 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
##slow chasses 2 step slower than the fast
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                return True
        return False