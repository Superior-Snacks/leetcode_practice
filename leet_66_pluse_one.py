def plusOne(digits):
    overflow = [1]
    for i in range(len(digits) -1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
            print(f"here {i}")
        elif digits[i] != 9:
            digits[i] += 1
            return digits
    digits.insert(0,1)
    return digits


print(plusOne([8,9,9,9]))