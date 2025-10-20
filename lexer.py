# First iteration of a lexer!

code = "var x = 3 + 5"
i = 0
tokens = []

def tokenize(code):
    i = 0
    tokens = []
    KEYWORDS = {'var', 'func', 'if', 'return', 'pure', 'int', 'float', 'string'}

    # Identifiers
    while i < len(code):
        char = code[i]


        if char.isalpha():
            word = ""
            while i < len(code) and (code[i].isalpha() or code[i] == '_'):
                word += code[i]
                i += 1
            if word in KEYWORDS:
                tokens.append((f'KEYWORD_{word.upper()}', word))
                continue
            else:
                tokens.append(('Identifier', word))
                continue
        
        # Newlines
        elif char == "\n":
            tokens.append(('NEWLINE', None))
            i += 1
            continue

        # Comments
        elif char == '#':
            while i < len(code) and code[i] != '\n':
                i += 1
            continue

        # Numbers
        elif char.isdigit():

            number = ""
            while i < len(code) and code[i].isdigit():
                number += code[i]
                i += 1
            tokens.append(('NUMBER', number))
            continue

        # (Symbols Section)
        elif char == '+':
            tokens.append(('PLUS', None))
            i += 1
            continue
        elif char == '-':
            tokens.append(('MINUS', None))
            i += 1
            continue
        elif char == '*':
            tokens.append(('STAR', None))
            i += 1
            continue
        elif char == '/':
            tokens.append(('SLASH', None))
            i += 1
            continue
        # Handles strings
        elif char == '"':
            i += 1
            value = ""
            while i < len(code) and code[i] != '"':
                value += code[i]
                i += 1
            i += 1 # this skips the closing quote
            tokens.append(('STRING', value))
            continue


        # Handle multi-equals (Assignment section)
        elif char == '=':
            if i + 1 < len(code) and code[i + 1] == '=': # if 2 characters, and the second character is '=' then its '=='
                tokens.append(('DOUBLE_EQUALS', None))
                i += 2
                continue
            else:
                tokens.append((f'EQUALS', None))
                i += 1
                continue
        elif char == '!':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(('NOT_EQUALS', None))
                i += 2
                continue
            else:
                tokens.append(('NOT', None))
                i += 1
                continue
        elif char == '>':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(('GREATER_OR_EQUAL', None))
                i += 2
                continue
            else:
                tokens.append(('GREATER_THAN', None))
                i += 1
                continue
        elif char == '<':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(('LESS_OR_EQUAL', None))
                i += 2
                continue
            else:
                tokens.append(('LESS_THAN', None))
                i += 1
                continue
        elif char == ':':
            if i + 1 < len(code) and code[i + 1] == '=':
                tokens.append(("ASSIGNMENT", None))
                i += 2
                continue
            else:
                tokens.append(("COLON", None))
                i += 1
                continue


        # (Wrapping symbols section '()', '[]', '{}')
        elif char == '(':
            tokens.append(('LPAREN', None))
            i += 1
            continue
        elif char == ')':
            tokens.append(('RPAREN', None))
            i += 1
            continue
        elif char == '[':
            tokens.append(('LBRACKET', None))
            i += 1
            continue
        elif char == ']':
            tokens.append(('RBRACKET', None))
            i += 1
            continue
        elif char == '{':
            tokens.append(('LBRACE', None))
            i += 1
            continue
        elif char == '}':
            tokens.append(('RBRACE', None))
            i += 1
            continue

            
        elif char == ' ': # ignore Whitespaces
            i += 1 

        else:
            print(f'Unexpected character: {char}')
            i += 1

    return tokens
print(tokenize(code))