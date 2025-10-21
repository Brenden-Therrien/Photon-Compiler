# Learning to make a Interpreter!

Building a Interpreter from scratch, with JIT compilation and a VM to run it to understand how programming language work!
My end goal is to make **'Photon'** a Interpreted language that hopefully makes graphics easy and enforces behavioural purity for safer, more predictable code.

# Progress

- [x] Lexer
- [x] Parser - Currently have (Variable, mathmatic operations, assignments like 'float', 'int', 'string')
- [x] Compiler / VM - basic yet working
- [x] Main file - impimented, run from here and put your desired code in ("code = ''") in main.py

# Features so far:
**Lexer** handles:
1. variable with underscores
2. Numbers
3. Operators (+, -, *, /, =, ==, !=, <=, >=)
4. whitespace handling
5. Comments '#'
6. newlines '\n'
7. parentheses, breackets, braces
8. Keywords ('var', 'func', 'if', 'return', 'pure', 'int', 'float', 'string')

**Parser** handles:
1. numbers, operations
2. makes a proper AST
3. interprets simple mathmatical operations (+, -, *, /)

**"Compiler"**
Basic yet implimented

**VM (virtual machine)**
works with all things supported so far. Reads from compiler!