def max_areas(height):
    area = 0
    left =0
    right = len(height) - 1

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height

        if current_area > area:
            area = current_area
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return area

print(max_areas([1,8,6,2,5,4,8,3,7]))