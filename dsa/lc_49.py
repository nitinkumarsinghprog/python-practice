def group_anagran(strs):
    my_map = {}

    for char in strs:
        key = ''.join(sorted(char))

        if key not in my_map:
            my_map[key] = []
        my_map[key].append(char)
    return list(my_map.values())

print(group_anagran(["eat","tea","tan","ate","nat","bat"]))
