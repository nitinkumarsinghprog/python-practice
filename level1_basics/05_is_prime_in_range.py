

a = int(input("Enter the first No : "))
b = int(input("Enter the second No : "))

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True

for n in range(a, b+1):
    if is_prime(n):
        print(n)
    