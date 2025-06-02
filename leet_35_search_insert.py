def searchInsert( nums, target):
    place = 0
    current = None
    while place > len(nums):
        current = nums[place]
        if current == target:
            return place
        elif current > target:
            return place
        else:
            place += 1

print(searchInsert([1,2,3,4,5,6], 5))