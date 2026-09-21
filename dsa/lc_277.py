def duplicate(nums):
    my_set = set()

    for num in nums:
        if num in my_set:
            return True
        my_set.add(num)
    return False

print(duplicate([1,2,3,4,2]))
print(duplicate([1,2,3,4,5]))