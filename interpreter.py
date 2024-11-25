from ast_nodes import AssignNode, BinOpNode, PrintNode, VarNode, NumberNode, StringNode

class Interpreter:
    def __init__(self):
        self.variables = {}

    #Visits each node and dispatches to the appropriate method.
    def visit(self, node):
        if isinstance(node, list):
            for stmt in node:
                self.visit(stmt)
        elif isinstance(node, AssignNode):
            return self.visit_AssignNode(node)
        elif isinstance(node, PrintNode):
            return self.visit_PrintNode(node)
        elif isinstance(node, BinOpNode):
            return self.visit_BinOpNode(node)
        elif isinstance(node, VarNode):
            return self.visit_VarNode(node)
        elif isinstance(node, NumberNode):
            return self.visit_NumberNode(node)
        elif isinstance(node, StringNode):
            return self.visit_StringNode(node)
        else:
            raise Exception(f"No visit method for node type {type(node).__name__}")
        
    #Handling variable assignment.
    def visit_AssignNode(self, node):
        value = self.visit(node.expr)
        self.variables[node.var_name] = value
        return value
    
    #Handling print statement.
    def visit_PrintNode(self, node):
        value = self.visit(node.expr)
        print(value)
        return value
    
    #Handling binary operations.
    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op == '+':
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            return left / right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            if right == 0:
               raise Exception("Division by zero error")
            return left / right
        else:
            raise Exception(f"Unknown operator: {node.op}")
    
    def visit_VarNode(self, node):
        if node.var_name not in self.variables:
           raise Exception(f"Undefined variable: {node.var_name}")
        return self.variables[node.var_name]

    
    #Handling number nodes.
    def visit_NumberNode(self, node):
        return node.value
    
    #Handling string literals.
    def visit_StringNode(self, node):
        return node.value