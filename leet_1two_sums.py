class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        track = {}
        for current, number in enumerate(nums):
            check = target - number
            if check in track:
                return [track[check], current]
            
print("yo")
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    track = {}
    for current, number in enumerate(nums):
        check = target - number
        if check in track:
            return [track[check], current]
print(twoSum([2,5,7,10], 9))