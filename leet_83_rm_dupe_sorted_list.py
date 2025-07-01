#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Create linked list from list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        print(current.val)
        while True:
            if current.next:
                current = current.next
                next_value = current.val
                print(next_value)
            else:
                break
        return current.val

sol = Solution()

# Test case 1: Empty list
#head = build_linked_list([])
#result = sol.deleteDuplicates(head)
#print("Test case []:", linked_list_to_list(result), "Expected: []")

# Test case 2: Single node
#head = build_linked_list([1])
#result = sol.deleteDuplicates(head)
#print("Test case [1]:", linked_list_to_list(result), "Expected: [1]")

# Test case 3: No duplicates
#head = build_linked_list([1, 2, 3, 4])
#result = sol.deleteDuplicates(head)
#print("Test case [1, 2, 3, 4]:", linked_list_to_list(result), "Expected: [1, 2, 3, 4]")

# Test case 4: All duplicates
#head = build_linked_list([1, 1, 1, 1])
#result = sol.deleteDuplicates(head)
#print("Test case [1, 1, 1, 1]:", linked_list_to_list(result), "Expected: [1]")

# Test case 5: Mixed duplicates
head = build_linked_list([1, 1, 2, 3, 3, 4, 4, 4, 5])
result = sol.deleteDuplicates(head)
print("Test case [1, 1, 2, 3, 3, 4, 4, 4, 5]:", linked_list_to_list(result), "Expected: [1, 2, 3, 4, 5]")

# Test case 6: Duplicates at the end
#head = build_linked_list([1, 2, 3, 4, 4])
#result = sol.deleteDuplicates(head)
#print("Test case [1, 2, 3, 4, 4]:", linked_list_to_list(result), "Expected: [1, 2, 3, 4]")