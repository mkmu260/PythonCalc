#calculator.py
#A simple calculator app
#Manoj K, 8/3/21
num = '0'
num = num + '1'
print(num)
num = int(num)
print(num)
print("Welcome to Manoj's Calculator V69")
exitProgram = False
while(exitProgram == False):
    firstNum = input("Enter your first number (If you want to exit, enter exit): ")
    if(firstNum == "exit"):
        print("Thank you for using Manoj K Services inc.")
        exitProgram = True
    else:
        try:
            firstNum = int(firstNum)
        except ValueError:
            print("That is not a valid number")
        else:
            calcType = input("What calculation do you want to do? (enter the symbol): ")
            try:
                secondNum = int(input("Enter your second number: "))
            except ValueError:
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