#Equation Solver
#Todo
#Symbols next to each other

from tokens import Token
from tokens import Equation

#Change

#change2

equation = []

equationRaw = input("Equation: \n")

#parse
for char in equationRaw:
    if ord(char) >= 48 and ord(char) <= 57:
        #It is a number
        if len(equation) != 0 and equation[-1].isdigit():
            equation[-1] += char
        else:
            equation.append(char)
    else:
        #Symbol

        equation.append(char)


tokenedEquation = Equation()
for tokenRaw in equation:
    if tokenRaw.isdigit():
        #Is a number
        token = Token("num", int(tokenRaw))
    else:
        token = Token("symbol", tokenRaw)
    tokenedEquation.addToken(token)

tokenedEquation.printEquation()

