
def is_palindrom(str):
    left, right = 0, len(str) -1 

    while left < right:
        while left < right and not str[left].isalnum():
            left += 1
        while left < right and not str[right].isalnum():
            right -= 1
        if str[left].lower() != str[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(is_palindrom("A man, a plan, a canal: Panama"))
print(is_palindrom("race a car"))  