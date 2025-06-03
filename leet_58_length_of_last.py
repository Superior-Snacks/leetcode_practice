def lengthOfLastWord(s):
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i].isalpha():
            count += 1
        elif count > 0:
            return count
    return count


print(lengthOfLastWord("Hello World"))  # Expected: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Expected: 4
print(lengthOfLastWord("Hello"))  # Expected: 5
print(lengthOfLastWord("world        "))  # Expected: 5
print(lengthOfLastWord("a   b    c   d   e   "))  # Expected: 1
print(lengthOfLastWord("solo     "))  # Expected: 4
print(lengthOfLastWord("yes"))  # Expected: 3
print(lengthOfLastWord("word before    final"))  # Expected: 5
print(lengthOfLastWord("           word"))  # Expected: 4
s = "a " * 9999 + "end"
print(lengthOfLastWord(s))  # Expected: 3
print(lengthOfLastWord("     "))  # Behavior undefined per constraints, should never occur.
print(lengthOfLastWord("MiXeDCaSe"))  # Expected: 9