def is_anagram(s,t):
    if len(s) != len(t):
        return False
    count = {}

    for char in s:
        count[char] = (count.get(char) or 0) + 1

    for char in t:
        if not count.get(char):
            return False
        count[char] -= 1
    return True

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "bat"))