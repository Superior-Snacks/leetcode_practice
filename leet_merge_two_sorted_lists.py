# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    """Creates a singly-linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

# Example sorted linked lists you can use:
list1_values = [1, 2, 4]
list2_values = [1, 3, 4]

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

# You can also create empty lists:
# list1_empty = create_linked_list([])
# list2_empty = create_linked_list([])

# Or lists with different lengths and values:
# list1_longer = create_linked_list([1, 5, 8, 12])
# list2_shorter = create_linked_list([2, 7])

# Helper function to print a linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

#print("List 1:")
#print_linked_list(list1)
#print("\nList 2:")
#print_linked_list(list2)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Your merging logic will go here
        # You can now work with the 'list1' and 'list2' variables
        # which are the heads of the linked lists you created above.
        a = list1.val
        b = list2.val
        print(a, b)
        if a <= b:


        # For now, let's just return None as a placeholder
        return None

# Example of how you might call your mergeTwoLists function:
solution = Solution()
merged_list_head = solution.mergeTwoLists(list1, list2)

#print("\nMerged List:")
#print_linked_list(merged_list_head)