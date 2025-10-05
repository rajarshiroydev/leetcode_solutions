# Optimal solution
# Time complexity O(N)
# Space Complexity O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
