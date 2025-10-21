# Lexer

code = "var x = 3 + 5"
i = 0
tokens = []

def tokenize(code):
    line = 1
    column = 1
    i = 0
    tokens = []
    KEYWORDS = {'var', 'func', 'if', 'return', 'pure', 'int', 'float', 'string'}

    # Identifiers
    while i < len(code):
        char = code[i]


        if char.isalpha():
            start_column = column
            word = ""
            while i < len(code) and (code[i].isalpha() or code[i] == '_'):
                word += code[i]
                i += 1
                column += 1
            if word in KEYWORDS:
                tokens.append((f'KEYWORD_{word.upper()}', word, line, start_column))
                continue
            else:
                tokens.append(('IDENTIFIER', word, line, start_column))
                column += len(word)
                continue
        
        # Newlines
        elif char == "\n":
            tokens.append(('NEWLINE', '\\n', line, column))
            i += 1
            line += 1
            column = 1
            continue

        # Comments
        elif char == '#':
            while i < len(code) and code[i] != '\n':
                i += 1
                column += 1
            continue

        # Numbers
        elif char.isdigit():
            start_column = column
            number = ""
            has_dot = False

            while i < len(code) and (code[i].isdigit() or (code[i] == '.' and not has_dot)):
                if code[i] == '.':
                    has_dot == True
                number += code[i]
                i += 1
                column += 1
            tokens.append(('NUMBER', number, line, start_column))
            continue

        # (Symbols Section)
        elif char == '+':
            tokens.append(('PLUS', '+', line, column))
            i += 1
            column += 1
            continue
        elif char == '-':
            tokens.append(('MINUS', '-', line, column))
            i += 1
            column += 1
            continue
        elif char == '*':
            tokens.append(('STAR', '*', line, column))
            i += 1
            column += 1
            continue
        elif char == '/':
            tokens.append(('SLASH', '/', line, column))
            i += 1
            column += 1
            continue
        # Handles strings
        elif char == '"':
            i += 1
            value = ""
            while i < len(code) and code[i] != '"':
                value += code[i]
                i += 1
            i += 1 # this skips the closing quote
            tokens.append(('STRING', value, line, start_column))
            column += len(value) + 2 
            continue


        # Handle multi-equals (Assignment section)
        elif char == '=':
            if i + 1 < len(code) and code[i + 1] == '=': # if 2 characters, and the second character is '=' then its '=='
                tokens.append(('DOUBLE_EQUALS', '==', line, column))
                i += 2
                column += 2
                continue
            else:
                tokens.append((f'EQUALS', '=', line, column))
                i += 1
                column += 1
                continue
        elif char == '!':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(('NOT_EQUALS', '!=', line, column))
                i += 2
                column += 2
                continue
            else:
                tokens.append(('NOT', '!', line, column))
                i += 1
                column += 1
                continue
        elif char == '>':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(('GREATER_OR_EQUAL', '>=', line, column))
                i += 2
                column += 2
                continue
            else:
                tokens.append(('GREATER_THAN', '>', line, column))
                i += 1
                column += 1
                continue
        elif char == '<':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(('LESS_OR_EQUAL', '<=', line, column))
                i += 2
                column += 2
                continue
            else:
                tokens.append(('LESS_THAN', '<', line, column))
                i += 1
                column += 1
                continue
        elif char == ':':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(("ASSIGNMENT", ':=', line, column))
                i += 2
                column += 2
                continue
            else:
                tokens.append(("COLON", ':', line, column))
                i += 1
                column += 1
                continue


        # (Wrapping symbols section '()', '[]', '{}')
        elif char == '(':
            tokens.append(('LPAREN', '(', line, column))
            i += 1
            column += 1
            continue
        elif char == ')':
            tokens.append(('RPAREN', ')', line, column))
            i += 1
            column += 1
            continue
        elif char == '[':
            tokens.append(('LBRACKET', '[', line, column))
            i += 1
            column += 1
            continue
        elif char == ']':
            tokens.append(('RBRACKET', ']', line, column))
            i += 1
            column += 1
            continue
        elif char == '{':
            tokens.append(('LBRACE', '{', line, column))
            i += 1
            column += 1
            continue
        elif char == '}':
            tokens.append(('RBRACE', '}', line, column))
            i += 1
            column += 1
            continue

            
        elif char == ' ': # ignore Whitespaces
            i += 1 
            column += 1
            continue

        else:
            print(f'Unexpected character: {char} at line {line}, column {column}')
            i += 1
    tokens.append(('EOF', None, line, column))
    return tokens
print(tokenize(code))