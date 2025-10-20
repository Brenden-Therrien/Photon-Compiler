# Learning to make a Interpreter!

Building a Interpreter from scratch, with JIT compilation and a VM to run it to understand how programming language work!
My end goal is to make **'Photon'** a Interpreted language that hopefully makes graphics easy and enforces behavioural purity for safer, more predictable code.

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
5. Comments '#'
6. newlines '\n'
7. parentheses, breackets, braces

**Parser** handles:
1. numbers, operations
2. makes a proper AST
3. interprets simple mathmatical operations (+, -, *, /)

**"Compiler"**
(WIP)

**VM (virtual machine)**
(WIP)