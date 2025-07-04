def merge(nums1, m, nums2, n):
    if m > 0 and n == 0:
        print(nums1)
    elif n > 0 and m == 0:
        nums1 = nums2
        print(nums1)
    elif m > 0:
        #here real code, go from back m + n check last n1[:m] v n2
        l1 = m -1
        l2 = -1
        for i in range(m + n - 1, -1, -1):
            if nums2[l2] > nums1[l1]:
                nums1[i] = nums2[l2]
                l2 -= 1
            elif nums1[l1] > nums2[l2]:
                nums1[i] = nums1[l1]
                l1 -= 1
            else:
                nums1[i] = nums1[l1]
                l1 -= 1
    return nums1



# Example 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(f"input: [1,2,3,0,0,0], [2,5,6] =>{nums1}, expected: [1,2,2,3,5,6]")

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(f"input: [1], [] => {nums1}, expected: [1]")

# Example 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(f"input: [0], [1] => {nums1}, expected: [1]")

# Example 4
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
merge(nums1, m, nums2, n)
print(f"input: [4,5,6,0,0,0], [1,2,3] => {nums1}, expected: [1,2,3,4,5,6]")

# Example 5
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(f"input: [2,0], [1] => {nums1}, expected: [1,2]")

# Example 6
nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1
merge(nums1, m, nums2, n)
print(f"input: [1,2,4,5,6,0], [3] => {nums1}, expected: [1,2,3,4,5,6]")

# Example 7
nums1 = [0,0,0]
m = 0
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(f"input: [0,0,0], [2,5,6] => {nums1}, expected: [2,5,6]")

# Example 8
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [4,5,6,7]
n = 4
merge(nums1, m, nums2, n)
print(f"input: [1,2,3,0,0,0,0], [4,5,6,7] => {nums1}, expected: [1,2,3,4,5,6,7]")

# Example 9
nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3
merge(nums1, m, nums2, n)
print(f"input: [2,2,3,0,0,0], [1,5,6] => {nums1}, expected: [1,2,2,3,5,6]")

# Example 10
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
merge(nums1, m, nums2, n)
print(f"input: [-1,0,0,3,3,3,0,0,0], [1,2,2] => {nums1}, expected: [-1,0,0,1,2,2,3,3,3]")
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""