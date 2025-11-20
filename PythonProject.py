def Ali_Rehan():
    run_loop = True
    while run_loop:
        print("---Basic Arithmetic Calculator---")
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        if operation == '+':
            print("The sum is:", num1 + num2)
        elif operation == '-':
            print("The difference is:", num1 - num2)
        elif operation == '*':
            print("The product is:", num1 * num2)
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("The quotient is:", num1 / num2)
        else:
            print("Invalid operation.")
        do_again = str(input("Do you want to perform another operation? (yes/no): "))
        if do_again == "no":
            run_loop = False
            print("Terminating..........")
        elif do_again == "yes":
            print("Restarting........If you did not enter yes and are wondering why it restarted, then it is your punishment because I told you how and what you were supposed to enter and you did not follow the instructions.")