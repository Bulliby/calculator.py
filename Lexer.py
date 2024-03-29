# **************************************************************************** #
#                                                                              #
#                                                                              #
#    Lexer.py                                                                  #
#                                                         ________             #
#    By: bulliby <wellsguillaume+at+gmail.com>           /   ____/_  _  __     #
#                                                       /    \  _\ \/ \/ /     #
#    Created: 2019/03/02 19:55:28 by bulliby            \     \_\ \     /      #
#    Updated: 2019/03/02 19:55:33 by bulliby             \________/\/\_/       #
#                                                                              #
# **************************************************************************** #

class Token():
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def __str__(self):
        return 'This object is a Token of the type {type}  with value {value}'.format(type=self.token, value=self.value)

class Lexer():
    def __init__(self, userInput):
        self.userInput = userInput
        self.pos = 0
        self.len = len(self.userInput)

    def __str__(self):
        return "This object transform the user input in Lexems"

    def currentChar(self):
        return self.userInput[self.pos]

    def advance(self):
        self.pos += 1

    def splitInput(self):
        tokens = []
        while self.pos < self.len:
            if self.currentChar().isdigit():
                tokens.append(Token('INT', self.handleInteger()))
            elif self.currentChar() == '+':
                tokens.append(Token('PLUS', self.handleOperator()))
            elif self.currentChar() == '-':
                tokens.append(Token('MINUS', self.handleOperator()))
            elif self.currentChar() == '/':
                tokens.append(Token('DIV', self.handleOperator()))
            elif self.currentChar() == '*':
                tokens.append(Token('MUL', self.handleOperator()))
            else:
                raise Exception("Invalid Character")
        tokens.append(Token(None, 0))
        return tokens

    def handleInteger(self):
        integer = ""
        while self.pos < self.len and self.currentChar().isdigit():
            integer += self.currentChar()
            self.advance()
        return integer

    def handleOperator(self):
        operator = self.currentChar()
        self.advance()
        return operator

    def handleWhiteSpace(self):
        while self.currentChar().isspace():
            self.advance()
