
def removeElement(nums, val):
    search = 0
    point = len(nums)
    print(point)
    while search != point:
        point -= 1
        while nums[point] == val:
            point -= 1
        if nums[search] == val:
            nums[search], nums[point] = nums[point], nums[search]
            search += 1
    print(nums)




removeElement([3,2,2,3], 3)
removeElement([3,4,8,8], 8)
removeElement([1,2,3,4,5,6,6,4], 6)
removeElement([1,1,1,2,2,2,4,4,1], 1)
removeElement([1,1,1,1], 3)