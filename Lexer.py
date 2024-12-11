from Token import *

#Create Lexer class and assign self variables when initialised
class Lexer:
    def __init__(self, script: str) -> None: 
        self.script: str = script
        self.index: int = 0
        self.char: str = ''
        self.tokens: list[Token] = []
    
    #Create function to progress character
    def advance(self) -> None:
        self.index += 1
        self.char = self.script[self.index]
    
    #Add token to self.tokens
    def add_token(self, char: str) -> None:
        self.tokens.append(char)