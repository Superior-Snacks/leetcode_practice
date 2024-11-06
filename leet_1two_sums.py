def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    track = {}
    for current, number in enumerate(nums):
        print(2)
        check = target - number
        if check in track:
            print(1)
            return [track[check], current]
        track[number] = check
print(twoSum([2,7,11,15], 9))