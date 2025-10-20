# Learning to make a compiler!

Building a compiler rom scratch to understand how programming language work!
My end goal is to make **'Photon'** a graphics-focused programming language

# Progress

- [x] Lexer
- [x] Parser - got a basic one working right now, basic AST with simple mathmatical operations supported
- [ ] Code Generator (Doing this next, currently just an interpreter)

# Features so far:
**Lexer** handles:
1. variable with underscores
2. Numbers
3. Operators (+, -, *, /, =, ==, !=, <=, >=)
4. whitespace handling

**Parser** handles:
1. numbers, operations
2. makes a proper AST
3. interprets simple mathmatical operations (+, -, *, /)