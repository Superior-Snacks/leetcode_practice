def addBinary(a, b):
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    result = ""
    
    while (i >= 0) and (j >= 0):
        if carry + int(a[i]) + int(b[j]) == 3:
            print("leave 1 carry 1")
            result = "1" + result
            carry = 1
            print(result)
        elif carry + int(a[i]) + int(b[j]) == 2:
            print("leave 0 carry 1")
            result = "0" + result
            carry = 1
            print(result)
        elif carry + int(a[i]) + int(b[j]) == 1:
            print("leave 1 carry 0")
            result = "1" + result
            carry = 0
            print(result)
        elif carry + int(a[i]) + int(b[j]) == 0:
            print("leave 0 carry 0")
            result = "0" + result
            carry = 0
            print(result)
        else:
            print("how the hell did you get here?!")
        i -= 1
        j -= 1

    if i >= 0:
        while carry != 0 and i >= 0:
            if carry + int(a[i]) == 2:
                print("leave 0 carry 1")
                result = "0" + result
                carry = 1
                print(result)
            elif carry + int(a[i]) == 1:
                print("leave 1 carry 0")
                result = "1" + result
                carry = 0
                print(result)
            elif carry + int(a[i]) == 0:
                print("leave 0 carry 0")
                result = "0" + result
                carry = 0
                print(result)
            else:
                print("how the hell did you get here?!")
            i -= 1
        if carry == 0:
            result = a[:i] + result
            print(result)
        else:
            result = "1" + result
            print(result)
    elif j >= 0:
        while carry != 0 and j >= 0:
            if carry + int(b[j]) == 2:
                print("leave 0 carry 1")
                result = "0" + result
                carry = 1
                print(result)
            elif carry + int(b[j]) == 1:
                print("leave 1 carry 0")
                result = "1" + result
                carry = 0
                print(result)
            elif carry + int(b[j]) == 0:
                print("leave 0 carry 0")
                result = "0" + result
                carry = 0
                print(result)
            else:
                print("how the hell did you get here?!")
            j -= 1
        if carry == 0:
            result = b[:j] + result
            print(result)
        else:
            result = "1" + result
            print(result)
    elif carry == 1:
        result = "1" + result
    print(f"result: {result}")
    return result

"""
how to calc binary, start from back if 1 + 1 leave 0 carry over 1 elif 1 + 0 leave 1 carry over none
a	b	in	sum	out
0	0	0	0	0
0	1	0	1	0
1	0	0	1	0
1	1	0	0	1
1	1	1	1	1
1	0	1	0	1
0	1	1	0	1
0	0	1	1	0
"""
print(addBinary("0", "0"), "=> 0")
print(addBinary("1", "0"), "=> 1")
print(addBinary("1", "1"), "=> 10")
print(addBinary("101", "1"), "=> 110")
print(addBinary("11", "1"), "=> 100")
print(addBinary("1", "111"), "=> 1000")
print(addBinary("1111", "1"), "=> 10000")
print(addBinary("111", "111"), "=> 1110")
a = "1" * 10  # 10 ones
b = "1"
# 1111111111 + 1 = 10000000000 (a 1 followed by ten 0s)
print(addBinary(a, b), "=> 10000000000")
print(addBinary("000", "000"), "=> 0")
print(addBinary("0001", "0010"), "=> 11")
"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""