def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    output = []
    remainder2 = []
    remainder1 = []
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            output.extend(remainder1)
            output.extend(list1[i])
            remainder2.extend(list2[i])
            remainder1 = []
        elif list2[i] < list1[i]:
            output.extend(remainder2)
            output.extend(list2[i])
            remainder1.extend(list1[i])
            remainder2 = []
        else:
            output.extend(remainder1)
            output.extend(remainder2)
            remainder1 = []
            remainder2 = []
    return output

print(mergeTwoLists([1,2,4],[1,3,4]))