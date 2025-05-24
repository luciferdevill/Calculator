# This code is a simple calculator that performs basic arithmetic operations
while True:
    a, b = map(int, input("Enter two numbers you want to calculate: ").split())
    
    while True:
        choice = input("Enter the operation you want to perform {+, -, *, /}: ")
        
        if choice == '+':
            add = lambda a, b: a + b
            result = add(a, b)
            print(f"The sum of {a} and {b} is: \033[1m{result}\033[0m")
        elif choice == '-':
            sub = lambda a, b: a - b
            result = sub(a, b)
            print(f"The difference of {a} and {b} is: \033[1m{result}\033[0m")
        elif choice == '*':
            mul = lambda a, b: a * b
            result = mul(a, b)
            print(f"The product of {a} and {b} is: \033[1m{result}\033[0m")
        elif choice == '/':
            if b == 0:
                print("Division by zero is not allowed.")
                break
            div = lambda a, b: a / b
            result = div(a, b)
            print(f"The division of {a} and {b} is: \033[1m{result}\033[0m")
        else:
            print("Invalid operation. Please enter one of the following: +, -, *, /")
            continue

        cont = input("""Do you want to perform with 
                                    1)New number 
                                    2)Existing number 
                                    3)Exit 
                                (Select the optiton): """)
        if cont == '1':
            break
        elif cont == '2':
            continue
        else:
            print("Exiting the program.")
            exit()
# This code is a simple calculator that performs basic arithmetic operations
