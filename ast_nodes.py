class AssignNode:
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

    def __repr__(self):
        return f"AssignNode(var={self.var_name}, expr={repr(self.expr)})"


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        op_name = {
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MUL',
            '/': 'DIV'
        }.get(self.op, self.op)  # Map symbols to readable names
        return f"BinOpNode(left={repr(self.left)}, op={op_name}, right={repr(self.right)})"


class PrintNode:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"PrintNode(expr={repr(self.expr)})"


class VarNode:
    def __init__(self, var_name):
        self.var_name = var_name

    def __repr__(self):
        return f"VarNode({self.var_name})"


class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"  # Return the raw number value


class StringNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)  # Return the raw string value