# Naive solution
# Time complexity O(N) x (O(1) + O(1)) = O(N) # Looping through all the nodes, 
# checking if the node already exists in the dict, inserting the node in the dict
# Space complexity O(N) # storing all the nodes in the dict
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_index = {}
        temp = head
        index = 0
        while temp:
            if temp in node_index:
                return temp
            else:
                node_index[temp] = index
            temp = temp.next
            index += 1
        return None

# Optimal Solution
# Time complexity O(N) + O(N) = O(N) as the loops are sequential and not nested loops
# Space complexity O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None