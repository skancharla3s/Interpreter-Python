# main.py

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    print("Enter your code below (use ';' to separate statements, and type 'Done' after entering your code):")
    code = ""
    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break  # Handle end-of-file (Ctrl+D)
        if line.strip() == "Done":
            break
        code += line + " "  # Accumulate the input code

    if not code.strip():
        print("No code provided. Please provide code.")
        return

    # Check if the code ends with a semicolon
    if not code.strip().endswith(';'):
        print("Syntax Error: Code must end with a semicolon (';').")
        return

    try:
        # Lexical Analysis
        lexer = Lexer(code)
        tokens = lexer.generate_tokens()
        print("\n--- Lexical Analysis ---")
        print(f"Tokens: {tokens}")

        # Parsing
        parser = Parser(tokens)
        tree = parser.parse()
        print("\n--- Parsing ---")
        print(f"AST Tree: {tree}")

        # Interpretation
        interpreter = Interpreter()
        print("\n--- Interpretation ---")
        interpreter.visit(tree)
    except Exception as e:
        print("Invalid input. Please check the code you typed.")
        print(e)

if __name__ == "__main__":
    main()