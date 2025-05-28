
def removeElement(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            print(nums, val)
    i += 1



removeElement([3,2,2,3], 3)
removeElement([3,4,8,8], 8)
removeElement([1,2,3,4,5,6,6,4], 6)
removeElement([1,1,1,2,2,2,4,4,1], 1)
removeElement([1,1,1,1], 3)