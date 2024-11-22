from ast_nodes import AssignNode, BinOpNode, PrintNode, VarNode, NumberNode, StringNode
from lexer import Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        """Advances to the next token."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        """Parses the tokens into a list of AST nodes."""
        statements = []
        while self.current_token.type != Lexer.EOF:
            statements.append(self.parse_statement())
            if self.current_token.type == Lexer.SEMI:
                self.advance()
        return statements

    def parse_statement(self):
        """Parses a single statement."""
        if self.current_token.type == Lexer.LET:
            return self.parse_assignment()
        elif self.current_token.type == Lexer.PRINT:
            return self.parse_print()
        else:
            raise Exception("Invalid statement")

    def parse_assignment(self):
        """Parses a variable assignment."""
        self.advance()  # Skip 'let'
        if self.current_token.type != Lexer.ID:
            raise Exception("Expected identifier after 'let'")
        var_name = self.current_token.value
        self.advance()
        if self.current_token.type != Lexer.ASSIGN:
            raise Exception("Expected '=' after identifier")
        self.advance()
        expr = self.parse_expression()
        return AssignNode(var_name, expr)

    def parse_print(self):
        """Parses a print statement."""
        self.advance()  # Skip 'print'
        if self.current_token.type != Lexer.LPAREN:
            raise Exception("Expected '(' after 'print'")
        self.advance()
        expr = self.parse_expression()
        if self.current_token.type != Lexer.RPAREN:
            raise Exception("Expected ')' after expression")
        self.advance()
        return PrintNode(expr)

    def parse_expression(self):
        """Parses an expression handling '+' and '-' operators."""
        left = self.parse_term()
        while self.current_token.type in (Lexer.PLUS, Lexer.MINUS):
            op = self.current_token.value  # '+' or '-'
            self.advance()
            right = self.parse_term()
            left = BinOpNode(left, op, right)
        return left

    def parse_term(self):
        """Parses a term handling '*' and '/' operators."""
        left = self.parse_factor()
        while self.current_token.type in (Lexer.MUL, Lexer.DIV):
            op = self.current_token.value  # '*' or '/'
            self.advance()
            right = self.parse_factor()
            left = BinOpNode(left, op, right)
        return left

    def parse_factor(self):
        """Parses a factor which can be a number, variable, string, or an expression in parentheses."""
        token = self.current_token
        if token.type == Lexer.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == Lexer.STRING:
            self.advance()
            return StringNode(token.value)  # Return a StringNode for string literals
        elif token.type == Lexer.ID:
            self.advance()
            return VarNode(token.value)
        elif token.type == Lexer.LPAREN:
            self.advance()
            expr = self.parse_expression()
            if self.current_token.type != Lexer.RPAREN:
                raise Exception("Expected ')'")
            self.advance()
            return expr
        else:
            raise Exception("Invalid syntax")