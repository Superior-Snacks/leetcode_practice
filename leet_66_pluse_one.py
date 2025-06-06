def plusOne(digits):
    for i in range(len(digits) -1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        elif digits[i] != 9:
            digits[i] += 1
            return digits
    digits.insert(0,1)
    return digits


print(plusOne([1, 2, 3]))     # [1, 2, 4]
print(plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
print(plusOne([9]))           # [1, 0]
print(plusOne([1, 2, 9]))     # [1, 3, 0]
print(plusOne([9, 9]))        # [1, 0, 0]
print(plusOne([2, 9, 9]))     # [3, 0, 0]
print(plusOne([9, 9, 9]))     # [1, 0, 0, 0]
print(plusOne([9]*10))       # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(plusOne([0]))           # [1]
print(plusOne([1]))           # [2]
print(plusOne([8]))           # [9]
print(plusOne([1]*99 + [2]))  # ends in [1]*99 + [3]