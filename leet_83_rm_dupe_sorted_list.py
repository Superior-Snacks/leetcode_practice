#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution(object):
    def deleteDuplicates(self, head):
        ...


sol = Solution()

# Test case 1: Empty list
head = build_linked_list([])
result = sol.deleteDuplicates(head)
print("Test case 1:", linked_list_to_list(result), "Expected: []")

# Test case 2: Single node
head = build_linked_list([1])
result = sol.deleteDuplicates(head)
print("Test case 2:", linked_list_to_list(result), "Expected: [1]")

# Test case 3: No duplicates
head = build_linked_list([1, 2, 3, 4])
result = sol.deleteDuplicates(head)
print("Test case 3:", linked_list_to_list(result), "Expected: [1, 2, 3, 4]")

# Test case 4: All duplicates
head = build_linked_list([1, 1, 1, 1])
result = sol.deleteDuplicates(head)
print("Test case 4:", linked_list_to_list(result), "Expected: [1]")

# Test case 5: Mixed duplicates
head = build_linked_list([1, 1, 2, 3, 3, 4, 4, 4, 5])
result = sol.deleteDuplicates(head)
print("Test case 5:", linked_list_to_list(result), "Expected: [1, 2, 3, 4, 5]")

# Test case 6: Duplicates at the end
head = build_linked_list([1, 2, 3, 4, 4])
result = sol.deleteDuplicates(head)
print("Test case 6:", linked_list_to_list(result), "Expected: [1, 2, 3, 4]")