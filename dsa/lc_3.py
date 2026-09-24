def longest_substring(s):
    left = 0
    max_count = 0
    my_set = set()

    for right in range(len(s)):
        while s[right] in my_set:
            my_set.remove(s[left])
            left += 1
        my_set.add(s[right])

        count = right - left + 1

        if count > max_count:
            max_count = count
    return max_count

print(longest_substring("abcabcbb"))