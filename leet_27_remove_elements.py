
def removeElement(nums, val):
    search = 0
    point = len(nums) - 1 
    while search <= point:
        while 0 <= point and nums[point] == val:
            point -= 1
        if nums[search] == val:
            nums[search], nums[point] = nums[point], nums[search]
            search += 1
            point -= 1
        else:
            search += 1
    return point + 1




print(removeElement([3,2,2,3], 3))
print(removeElement([3,4,8,8], 8))
print(removeElement([1,2,3,4,5,6,6,4], 6))
print(removeElement([1,1,1,2,2,2,4,4,1], 1))
print(removeElement([1,1,1,1], 3))
print(removeElement([3,3], 3))
print(removeElement([2], 2))
print(removeElement([], 0))
print(removeElement([1,2,3,4], 5))