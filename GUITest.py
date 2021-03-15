#GUITest.py
#Started off as a way of testing PyQt5, now is a functioning graphical application calculator
#Manoj K, 11/03/2021

from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QWidget, QPushButton, QMessageBox

def button1Pressed(): #Need to find way to read button string so that one func can be used for all
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('1')

    if(isFirstNumber):
        firstNumber = firstNumber + '1'
    else:
        secondNumber = secondNumber + '1'

def button2Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('2')

    if(isFirstNumber):
        firstNumber = firstNumber + '2'
    else:
        secondNumber = secondNumber + '2'

def button3Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('3')

    if(isFirstNumber):
        firstNumber = firstNumber + '3'
    else:
        secondNumber = secondNumber + '3'

def button4Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('4')
    
    if(isFirstNumber):
        firstNumber = firstNumber + '4'
    else:
        secondNumber = secondNumber + '4'

def button5Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('5')

    if(isFirstNumber):
        firstNumber = firstNumber + '5'
    else:
        secondNumber = secondNumber + '5'

def button6Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('6')
    
    if(isFirstNumber):
        firstNumber = firstNumber + '6'
    else:
        secondNumber = secondNumber + '6'

def button7Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('7')
    
    if(isFirstNumber):
        firstNumber = firstNumber + '7'
    else:
        secondNumber = secondNumber + '7'

def button8Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('8')
    
    if(isFirstNumber):
        firstNumber = firstNumber + '8'
    else:
        secondNumber = secondNumber + '8'

def button9Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('9')
    
    if(isFirstNumber):
        firstNumber = firstNumber + '9'
    else:
        secondNumber = secondNumber + '9'

def button0Pressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global displayLabel = QLabel('0') #INstead update QLabel with firstNumber/secondNumber to display full number
    
    if(isFirstNumber):
        firstNumber = firstNumber + '0'
    else:
        secondNumber = secondNumber + '0'

def buttonPlusPressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global calcType
    
    if(isFirstNumber):
        calcType = '+'
        isFirstNumber = False
    else:
        alert = QMessageBox()
        alert.setText('You have already selected a function')
        alert.exec()

def buttonMinusPressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global calcType
    
    if(isFirstNumber):
        calcType = '-'
        isFirstNumber = False
    else:
        alert = QMessageBox()
        alert.setText('You have already selected a function')
        alert.exec()

def buttonMultPressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global calcType
    
    if(isFirstNumber):
        calcType = '*'
        isFirstNumber = False
    else:
        alert = QMessageBox()
        alert.setText('You have already selected a function')
        alert.exec()

def buttonDivPressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global calcType
    
    if(isFirstNumber):
        calcType = '/'
        isFirstNumber = False
    else:
        alert = QMessageBox()
        alert.setText('You have already selected a function')
        alert.exec()

def buttonEqualPressed():
    global isFirstNumber
    global firstNumber
    global secondNumber
    global calcType
    
    if(~isFirstNumber): #Add textbox with input number/answer
        firstNumber = int(firstNumber)
        secondNumber = int(secondNumber)
        if calcType == '+':
            output = firstNumber + secondNumber
        elif calcType == '-':
            output = firstNumber - secondNumber #Replace with switchcase
        elif calcType == '*':
            output = firstNumber * secondNumber
        elif calcType == '/':
            output = firstNumber / secondNumber #Add ability to continously add etc numbers
        answer = QMessageBox()
        answerMessage = str(firstNumber) + ' '  + calcType + ' ' + str(secondNumber) + ' = ' + str(output)
        answer.setText(answerMessage)
        answer.exec()
        isFirstNumber = True #Add clear button. May also clash with formatting (int + str). Could resolve by converting back to string after calcs
        firstNumber = '0'
        secondNumber = '0'
    else:
        alert = QMessageBox()
        alert.setText('You haven''t chosen an operation and/or a second number')
        alert.exec()

#Main Routine

firstNumber = '0' #Could pass and return these rather than using as global var
secondNumber = '0'
isFirstNumber = True

app = QApplication([])
window = QWidget() 
layout = QGridLayout()

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
buttonPlus = QPushButton('+')
button4 = QPushButton('4')
button5 = QPushButton('5')
button6 = QPushButton('6')
buttonMinus = QPushButton('-')
button7 = QPushButton('7')
button8 = QPushButton('8')
button9 = QPushButton('9')
buttonMult = QPushButton('*')
button0 = QPushButton('0')
buttonDiv = QPushButton('/')
buttonEqual = QPushButton('=')
displayLabel = QLabel("Test")

layout.addWidget(displayLabel, 3, 3)
layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 0, 1)
layout.addWidget(button3, 0, 2)
layout.addWidget(buttonPlus, 0, 3)
layout.addWidget(button4, 1, 0)
layout.addWidget(button5, 1, 1)
layout.addWidget(button6, 1, 2)
layout.addWidget(buttonMinus, 1, 3)
layout.addWidget(button7, 2, 0)
layout.addWidget(button8, 2, 1)
layout.addWidget(button9, 2, 2)
layout.addWidget(buttonMult, 2, 3)
layout.addWidget(button0, 3, 0)
layout.addWidget(buttonDiv, 3, 1)
layout.addWidget(buttonEqual, 3, 2)

button1.clicked.connect(button1Pressed)
button2.clicked.connect(button2Pressed)
button3.clicked.connect(button3Pressed)
button4.clicked.connect(button4Pressed)
button5.clicked.connect(button5Pressed)
button6.clicked.connect(button6Pressed)
button7.clicked.connect(button7Pressed)
button8.clicked.connect(button8Pressed)
button9.clicked.connect(button9Pressed)
button0.clicked.connect(button0Pressed)
buttonPlus.clicked.connect(buttonPlusPressed)
buttonMinus.clicked.connect(buttonMinusPressed)
buttonMult.clicked.connect(buttonMultPressed)
buttonDiv.clicked.connect(buttonDivPressed)
buttonEqual.clicked.connect(buttonEqualPressed)


window.setLayout(layout)
window.show()
#label = QLabel('Hello World!')
#label.show()
app.exec_()
