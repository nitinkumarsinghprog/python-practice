

a = int(input("Enter the first no: "))
b = int(input("Enter the second no: "))

while True:
    print("Please select one option ")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    option = int(input("Your Option: "))

    if option == 1:
        result = a + b

    elif option == 2:
        result = a - b

    elif option == 3:
        result = a * b

    elif option == 4:
        result = a / b

    else:
        print("Please select a valid option")
        continue

    print("Result:", result)
    break