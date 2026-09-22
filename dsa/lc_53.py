def largest_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    start = 0
    end = 0

    for i in range(1,len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start = i
        else:
            current_sum = current_sum + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end = i
    return max_sum, nums[start:end+1]

print(largest_sum([-2,1,-3,4,-1,2,1,-5,4]))

