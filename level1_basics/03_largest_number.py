
print("Enter 3 or more values for comprasion with space seprated")
nums = list(map(int, input("Enter numbers : ").split()))

largest_number = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest_number:
        largest_number = nums[i]

print(largest_number)