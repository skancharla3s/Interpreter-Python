class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}" if self.value is not None else f"{self.type}"

class Lexer:
    # Define Token Types
    LET = 'LET'
    PRINT = 'PRINT'
    ID = 'ID'
    ASSIGN = 'ASSIGN'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    DIV = 'DIV'
    SEMI = 'SEMI'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        #Advances the position pointer and updates the current character.
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        #Skips whitespace characters in the input code.
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def generate_tokens(self):
        #Tokenizes the input code into meaningful symbols.
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
            elif self.current_char.isdigit():
                tokens.append(self.generate_number())
            elif self.current_char.isalpha():
                tokens.append(self.generate_identifier())
            elif self.current_char == '+':
                tokens.append(Token(self.PLUS, '+'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(self.MINUS, '-'))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(self.MUL, '*'))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(self.DIV, '/'))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(self.ASSIGN, '=')) 
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token(self.SEMI, ';'))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(self.LPAREN, '('))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(self.RPAREN, ')'))
                self.advance()
            elif self.current_char == '"':
                tokens.append(self.generate_string())
            else:
                raise Exception(f"Invalid character: {self.current_char}")
        tokens.append(Token(self.EOF))
        return tokens

    def generate_number(self):
        #Parses multi-digit numbers.
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return Token(self.NUMBER, int(num_str))

    def generate_identifier(self):
        #Recognizes keywords or variable names (identifiers).
        id_str = ''
        while self.current_char is not None and self.current_char.isalnum():
            id_str += self.current_char
            self.advance()
        if id_str == 'let':
            return Token(self.LET, 'let')
        elif id_str == 'print':
            return Token(self.PRINT, 'print')
        return Token(self.ID, id_str)

    def generate_string(self):
        #Parses a string literal.
        self.advance()
        string_val = ''
        while self.current_char is not None and self.current_char != '"':
            string_val += self.current_char
            self.advance()
        self.advance()
        return Token(self.STRING, string_val)