# This is simple calculator

flag = False
while True:
    print('''\nSelect operation
        [N] Enter numbers
        [+] Add
        [-] Subtract
        [*] Multiply
        [/] Divide
        [X] Quit ''')

    choice = input("\nYour option: ")
    if choice.upper() == 'N':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        input()
        flag = True

    elif choice == '+' and flag == True:
        print(num1, "+", num2, "=", num1 + num2)
        input()

    elif choice == '-' and flag == True:
        print(num1, "-", num2, "=", num1 - num2)
        input()

    elif choice == '*' and flag == True:
        print(num1, "*", num2, "=", num1 * num2)
        input()

    elif choice == '/' and flag == True:
        print(num1, "/", num2, "=", num1 / num2)
        input()

    elif choice.upper() == 'X':
        print("Quitting program...")
        break 

    elif flag == False:
        if choice in ('+', '-', '*', '/'):
            print("No numbers entered")
            input()
        else:
            print("Invalid option")
            input()

    else:
        print("Invalid operation")
        input()