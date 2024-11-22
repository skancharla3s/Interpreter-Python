class AssignNode:
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class PrintNode:
    def __init__(self, expr):
        self.expr = expr

class VarNode:
    def __init__(self, var_name):
        self.var_name = var_name

class NumberNode:
    def __init__(self, value):
        self.value = value

class StringNode:
    def __init__(self, value):
        self.value = value  # New node type for string literals