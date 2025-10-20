# First iteration of a lexer!

code = "hello_x = 3 + 5 - 10 * 3 / 6"
i = 0
tokens = []

# Identifiers
while i < len(code):
    char = code[i]

    if char.isalpha():
        word = ""
        while i < len(code) and (code[i].isalpha() or code[i] == '_'):
            word += code[i]
            i += 1
        tokens.append(('[Identifier]', word))

    # Numbers
    if char.isdigit():

        number = ""
        while i < len(code) and code[i].isdigit():
            number += code[i]
            i += 1
        tokens.append(('[NUMBER]', number))

    # operators / symbols
    elif char == '+':
        tokens.append(('[PLUS]', None))
        i += 1
    elif char == '-':
        tokens.append(('[MINUS]', None))
        i += 1
    elif char == '*':
        tokens.append(('[STAR]', None))
        i += 1
    elif char == '/':
        tokens.append(('[SLASH]', None))
        i += 1
    # Handle multi-equals 
    elif char == '==':
        if i + 1 < len(code) and code[i + 1] == '=': # if 2 characters, and the second character is '=' then its '=='
            tokens.append(('[DOUBLE_EQUALS]', None))
            i += 2
        else:
            tokens.append((f'[EQUALS]', None))
            i += 1
    elif char == '!':
        if i + 1 < len(code) and code[i + 1] == '=':
            tokens.append(('[NOT_EQUALS]', None))
            i += 1
        else:
            tokens.append(('[NOT]', None))
            i += 1
    elif char == '>':
        if i + 1 < len(code) and code[i + 1] == '=':
            tokens.append(('[GREATER_OR_EQUAL]', None))
            i += 2
        else:
            tokens.append(('[GREATER_THAN]', None))
            i += 1
    elif char == '<':
        if i + 1 < len(code) and code[i + 1] == '=':
            tokens.append(('[LESS_OREQUAL]', None))
            i += 2
        else:
            tokens.append(('[LESS_THAN]', None))
            i += 1
    elif char == ' ': # ignore Whitespaces
        i += 1 
    else:
        print(f'Unexpected character: {char}')
        i += 1

print(tokens)