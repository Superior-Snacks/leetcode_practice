# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(head):
    head1 = ListNode(head[0])

    for i in head[1:]:
        print(i)
        head1.next = i
        head1 = head1

    print(head1.val, "error")
    return head1

def attach_lists(headA, headB, skipA, skipB):
    ...

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """


sol = Solution()

# Example 1
headA1 = create_linked_list([4,1,8,4,5])
headB1 = create_linked_list([5,6,1])
attach_lists(headA1, headB1, skipA=2, skipB=2)
print(sol.getIntersectionNode(headA1, headB1).val, "expected 8")

# Example 2
headA2 = create_linked_list([1,9,1,2,4])
headB2 = create_linked_list([3])
attach_lists(headA2, headB2, skipA=3, skipB=0)
print(sol.getIntersectionNode(headA2, headB2).val, "expected 2")

# Example 3 (no intersection)
headA3 = create_linked_list([2,6,4])
headB3 = create_linked_list([1,5])
print(sol.getIntersectionNode(headA3, headB3), "expected None")

# Intersect at head
headA4 = create_linked_list([1,2,3])
headB4 = headA4   # both point to the same head
print(sol.getIntersectionNode(headA4, headB4).val, "expected 1")

# Single-node lists, no intersection
headA5 = create_linked_list([7])
headB5 = create_linked_list([7])  # different node object
print(sol.getIntersectionNode(headA5, headB5), "expected None")

# Uneven lengths, late intersection
headA6 = create_linked_list([0,0,0,0,0,9,10,11])
headB6 = create_linked_list([7])
attach_lists(headA6, headB6, skipA=5, skipB=0)
print(sol.getIntersectionNode(headA6, headB6).val, "expected 9")

# Long disjoint lists
headA7 = create_linked_list(list(range(1, 1001)))
headB7 = create_linked_list(list(range(1001, 2001)))
print(sol.getIntersectionNode(headA7, headB7), "expected None")

# Intersection at tail
headA8 = create_linked_list([8,2,3])
headB8 = create_linked_list([6,7,5])
attach_lists(headA8, headB8, skipA=2, skipB=2)
print(sol.getIntersectionNode(headA8, headB8).val, "expected 3")
"""
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, 
headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B 
(2nd node in A and 3rd node in B) are different node references. In other words, 
they point to two different locations in memory, while the nodes with value 8 in A and B 
(3rd node in A and 4th node in B) point to the same location in memory.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 
Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""