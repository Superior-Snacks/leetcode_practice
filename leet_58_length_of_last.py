def lengthOfLastWord(self, s):
    ...



print(lengthOfLastWord("Hello World"))  # Expected: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Expected: 4
print(lengthOfLastWord("Hello"))  # Expected: 5
print(lengthOfLastWord("world        "))  # Expected: 5
print(lengthOfLastWord("a   b    c   d   e   "))  # Expected: 1
print(lengthOfLastWord("solo     "))  # Expected: 4
print(lengthOfLastWord("yes"))  # Expected: 3
print(lengthOfLastWord("word before    final"))  # Expected: 5
print(lengthOfLastWord("           word"))  # Expected: 4
print(lengthOfLastWord("a " * 9999 + "end"))  # Expected: 3
print(lengthOfLastWord("     "))  # Behavior undefined per constraints, should never occur.
print(lengthOfLastWord("MiXeDCaSe"))  # Expected: 9