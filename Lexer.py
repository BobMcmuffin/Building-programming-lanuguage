from Token import *

#Create Lexer class and assign self variables when initialised
class Lexer:
    def __init__(self, script: str) -> None: 
        self.script: str = script
        self.index: int = 0
        self.char: str = ''
        self.tokens: list[Token] = []

    #Creates function to read word by word
    def append_word(self) -> None:
        with open(self.script, 'r') as script:
            for line in script:
                for word in line.split():
                    self.tokens.append(word)
    
    #Create function to progress character
    def advance(self) -> None:
        self.char = self.script[self.index]
        self.index += 1
        
    
    #Add token to self.tokens
    def add_token(self, char: str) -> None:
        #Spaces aren't required as tokens so do not get added to self.tokens
        if char != ' ':
            self.tokens.append(char)
        else:
            pass
    
    #Clear original self.char from list - to be removed when alternative method found
    def remove_original(self) -> None:
        self.tokens.pop(0)

    #Read self.script and append self.tokens for each char
    def read_script(self) -> None:
        self.tokens.append(self.char)
        while self.index < len(self.script):
            self.advance()
            self.add_token(self.char)
        self.remove_original()
