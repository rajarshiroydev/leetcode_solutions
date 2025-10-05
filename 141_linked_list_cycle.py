# Naive solution
# Time complexity O(N) x (O(1) + O(1)) = O(N) # Looping through all the nodes, 
# checking if the node already exists in the dict, inserting the node in the dict
# Space complexity O(N) # storing all the nodes in the dict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_list = {}
        temp = head
        while temp:
            if temp in node_list:
                return True
            else:
                node_list[temp] = 1
            temp = temp.next
        return False


# Optimal solution
# Time complexity O(N)
# Space complexity O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False