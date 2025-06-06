def plusOne(digits):
    for i in range(len(digits) -1, -1, -1):
        if i == 9:
            digits[i] = 0
        elif i != 9:
            digits[i] += 1



print(plusOne([1,2,3]))