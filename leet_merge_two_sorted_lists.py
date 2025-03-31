def mergeTwoLists(self, list1, list2):
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
            output.append(remainder1)
            output.append(list1[i])
            remainder.append(list2[i])
        elif list2[i] < list1[i]:
            output.append(remainder2)
            output.append(list2[i])
            remainder1.append(list1[i])
        else:
            output.append(remainder1,remainder2)
            remainder1 = []
            remainder2 = []

mergeTwoLists(list1, list2)
mergeTwoLists(list1, list2)
mergeTwoLists(list1, list2)