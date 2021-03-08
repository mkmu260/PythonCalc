print("Welcome to Manoj's Calculator V69")
exitProgram = False
while(exitProgram == False):
    try:
        firstNum = int(input("Enter your first number (If you want to exit, enter exit): "))
    except ValueError:
        print("Thank you for using Manoj K Services inc.")
        exitProgram = True
    else:
        calcType = input("What calculation do you want to do? (enter the symbol): ")
        try:
            secondNum = int(input("Enter your second number: "))
        except:
            print("That is not a valid number")
        else:

            if calcType == '+':
                output = firstNum + secondNum
            elif calcType == '-':
                output = firstNum - secondNum
            elif calcType == 'x':
                output = firstNum * secondNum
            elif calcType == '*':
                output = firstNum * secondNum
            elif calcType == '/':
                output = firstNum / secondNum
            try:
                print("The answer is:", output)
            except: 
                print("Your calculation type is invalid, please try again")