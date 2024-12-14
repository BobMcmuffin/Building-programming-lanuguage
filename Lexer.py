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

    #Cleanse self.tokens to ensure characters are separated from keywords
    def cleanse(self) -> None:
        letters: str = 'abcdefghijklmnopqrstuvwxyz'
        new_tokens = []  # Temporary list to hold tokens in correct order

        for token in self.tokens:
            current_token = ''  # To build valid parts of the token
            for char in token:
                if char.lower() in letters:  # Check if the character is alphabetic
                    current_token += char  # Add to the current valid token
                else:
                    if current_token:  # If there's a valid token fragment, save it
                        new_tokens.append(current_token)
                        current_token = ''  # Reset the current token
                    new_tokens.append(char)  # Add the non-alphabetic character as its own token
            if current_token:  # Append any remaining valid token fragment
                new_tokens.append(current_token)

        self.tokens = new_tokens  # Update the tokens with the newly constructed list

    #Read script and append tokens correctly, then cleanse and return self.tokens
    def read_script(self) -> list[Token]:
        self.append_word()
        self.cleanse()
        return self.tokens