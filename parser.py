# Parser

import lexer
tokens = [] # list from the lexer
position = 0
current_token = None
variables = {}

def advance():
    global position, current_token
    position += 1
    if position < len(tokens):
        current_token = tokens[position]
    else:
        current_token = None 

def parse_expression():
    # Get the left side which could be say... a number or multiplication
    left = parse_multiplication()

    if current_token and (current_token[0] == 'PLUS' or current_token[0] == 'MINUS'):
        operator = current_token
        advance() # advance just means move to the next token
        right = parse_expression()
        return (operator, left, right)

    return left # no operator, just returning the final output

def parse_multiplication():
    left = parse_number()

    if current_token and (current_token[0] == 'STAR' or current_token[0] == 'SLASH'):
        operator = current_token
        advance()
        right = parse_multiplication()
        return (operator, left, right)

    return left

def parse_number():
    if current_token and current_token[0] == 'NUMBER':
        value = current_token[1]
        advance()
        return ('NUMBER', value)
    
    # Handle identifiers (variables)
    elif current_token and current_token[0] == 'IDENTIFIER':
        var_name = current_token[1]
        advance()
        
        # Look up the variable
        if var_name not in variables:
            raise Exception(f"Variable '{var_name}' not defined")
        return ('VARIABLE', var_name)
    else:
        raise Exception(f"Expected number or variable, got {current_token}")

def parse_var_declaration():
    # expect: var IDENTIFIER TYPE = EXPRESSION

    if current_token[0] != 'KEYWORD_VAR':
        raise Exception("Expected 'var'")
    advance()

    if current_token[0] != 'IDENTIFIER':
        raise Exception("Expected identifier")
    var_name = current_token[1]
    advance()

    if current_token[0] not in ['KEYWORD_INT', 'KEYWORD_FLOAT', 'KEYWORD_STRING']:
        raise Exception(f"Expected type (int, float, string), got {current_token}")
    var_type = current_token[1]
    advance()

    if current_token[0] != 'EQUALS':
        raise Exception("Expected '=' after type")
    advance()

    # Parses the expression
    value_expr = parse_expression()

    variables[var_name] = {'type': var_type, 'expr': value_expr}
    return ('VAR_DECL', var_name, var_type, value_expr)

def evaluate(node):
    # if number, just return it
    if isinstance(node, tuple) and node[0] == 'NUMBER':
        return int(node[1]) # convert string to number

    if isinstance(node, tuple) and node[0] == 'VARIABLE':
        var_name = node[1]
        return variables[var_name]['value']

    # if not number, its an operator
    operator = node[0]
    left = evaluate(node[1])
    right = evaluate(node[2])

    if operator[0] == 'PLUS':
        return left + right
    elif operator[0] == 'MINUS':
        return left - right
    elif operator[0] == 'STAR':
        return left * right
    elif operator[0] == 'SLASH':
        return left / right
