def searchInsert(nums, target):
    pointerL = 0
    pointerR = len(nums)-1
    while True:
        mid = (pointerL + pointerR) // 2
        print(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            pointerR = mid - 1
        elif nums[mid] < target:
            pointerL = mid + 1









print(searchInsert([1, 2, 3, 4, 5, 6], 5))  # 4 (found at index 4)
print(searchInsert([10, 20, 30], 5))       # 0 (smaller than all elements)
print(searchInsert([1, 3, 5, 7], 6))        # 3 (between 5 and 7)
print(searchInsert([1, 3, 5, 7], 10))       # 4 (larger than all)
print(searchInsert([5, 10, 15], 5))         # 0
print(searchInsert([5, 10, 15], 15))        # 2
print(searchInsert([10], 5))               # 0
print(searchInsert([10], 15))              # 1
print(searchInsert([10], 10))              # 0
print(searchInsert([2, 4, 6, 8], 3))        # 1
print(searchInsert([], 5))                 # 0

def derepitSearchInsert( nums, target):
    place = 0
    current = None
    while place < len(nums):
        current = nums[place]
        if current == target:
            return place
        elif current > target:
            return place
        else:
            place += 1
    return place