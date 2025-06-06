def plusOne(digits):
    for i in range(len(digits) -1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
            print(f"here {i}")
        elif digits[i] != 9:
            digits[i] += 1
            return digits



print(plusOne([9,9,9,9]))