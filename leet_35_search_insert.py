def searchInsert( nums, target):
    place = 0
    current = None
    while place < len(nums):
        print(1)
        current = nums[place]
        if current == target:
            return place
        elif current > target:
            return place
        else:
            place += 1
    return place

print(searchInsert([1, 2, 3, 4, 5, 6], 5))  # 4 (found at index 4)