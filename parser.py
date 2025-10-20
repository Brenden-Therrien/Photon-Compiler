# Parser

import lexer
tokens = [] # list from the lexer
position = 0
current_token = None

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
    else:
        raise Exception(f"Expected number, got {current_token}")

def evaluate(node):
    # if number, just return it
    if isinstance(node, tuple) and node[0] == 'NUMBER':
        return int(node[1]) # convert string to number

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

tokens = lexer.tokenize("597 + 16 * 45 / 12") # example code
current_token = tokens[0] if tokens else None
tree = parse_expression()
print("AST:", tree)
result = evaluate(tree)
print("Result:", result)