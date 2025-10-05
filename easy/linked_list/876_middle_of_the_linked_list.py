# Naive Solution
# Time complexity O(N + N/2)
# Space complexity O(1)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length = length + 1
            current = current.next

        mid_index = length // 2
        current = head
        for _ in range(mid_index):
            current = current.next

        return current


# Optimal Solution (Tortoise and Hare solution)
# Time complexity O(N)
# Space complexity O(1)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_current = head
        fast_current = head
        while fast_current and fast_current.next:
            slow_current = slow_current.next
            fast_current = fast_current.next.next
        
        return slow_current
