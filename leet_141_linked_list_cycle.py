# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    fix = head
    current = head
    
    # build the chain
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    # only connect if pos >= 0
    if pos >= 0:
        fix = head
        for _ in range(pos):
            fix = fix.next
        current.next = fix
    
    return head

class Solution(object):
    def hasCycle(self, head):
        current_slow = head
        current_fast = head
        temp = []
        while current_fast != None:
            current_slow = current_slow.next
            current_fast = current_fast.nex.next
            if current_slow == current_fast:
                return True
        return False
            


sol = Solution()

# Example 1: cycle at pos=1
head = build_linked_list([3,2,0,-4], pos=1)
print(sol.hasCycle(head), "expected: True")

# Example 2: cycle at pos=0
head = build_linked_list([1,2], pos=0)
print(sol.hasCycle(head), "expected: True")

# Example 3: no cycle
head = build_linked_list([1], pos=-1)
print(sol.hasCycle(head), "expected: False")

# Edge case: empty list
head = build_linked_list([], pos=-1)
print(sol.hasCycle(head), "expected: False")

# Edge case: single node self-cycle
head = build_linked_list([1], pos=0)
print(sol.hasCycle(head), "expected: True")
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


"""
fyrsta tilraun
class Solution(object):
    def hasCycle(self, head):
        current = head
        temp = []
        while current != None:
            if current.next in temp:
                return True
            else:
                current = current.next
                temp.append(current)
        return False
"""