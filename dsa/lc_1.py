def two_sum(nums, target):
    my_map = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in my_map:
            return [my_map[diff], i]
        my_map[nums[i]] = i
    return []

print(two_sum([2,7,6,9], 9))
print(two_sum([2,7,8,6], 5))