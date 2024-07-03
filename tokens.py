class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value

class Equation:

    def __init__(self):
        self.equation = []
    def addToken(self, token):
        self.equation.append(token)

    def printEquation(self):
        for token in self.equation:
            print("(" + str(token.value) + "->" + token.type + ") ", end='')

        print("\n")

    def solve(self):
        start = 0

        while len(self.equation) > 1:
            pass
