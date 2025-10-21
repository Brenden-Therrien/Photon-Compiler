# compiler that outputs bytecode for vm to read

from opcodes import *

def compile_expression(node):
    instructions = []
    
    if node[0] == 'NUMBER':
        instructions.append((PUSH, int(node[1])))
    
    elif node[0] == 'VARIABLE':
        instructions.append((LOAD, node[1]))
    
    else:
        # It's an operation
        operator = node[0]
        left = node[1]
        right = node[2]
        
        # Compile left side
        instructions.extend(compile_expression(left))
        # Compile right side
        instructions.extend(compile_expression(right))
        
        # Add the operation
        if operator[0] == 'PLUS':
            instructions.append((ADD,))
        elif operator[0] == 'MINUS':
            instructions.append((SUB,))
        elif operator[0] == 'STAR':
            instructions.append((MUL,))
        elif operator[0] == 'SLASH':
            instructions.append((DIV,))
    
    return instructions

def compile_var_declaration(ast):
    # ast is ('VAR_DECL', var_name, var_type, expression)
    var_name = ast[1]
    expression = ast[3]
    
    instructions = []
    
    # Compile the expression (puts result on stack)
    instructions.extend(compile_expression(expression))
    
    # Store the result in the variable
    instructions.append((STORE, var_name))
    
    return instructions