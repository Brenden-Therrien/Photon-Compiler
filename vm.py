# Virtual machine that reads the bytecode

from opcodes import *

class VM:
    def __init__(self):
        self.stack = []
        self.variables = {}
    
    def execute(self, instructions):
        for instruction in instructions:
            opcode = instruction[0]
            
            if opcode == PUSH:
                value = instruction[1]
                self.stack.append(value)
            
            elif opcode == ADD:
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left + right)
            
            elif opcode == SUB:
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left - right)
            
            elif opcode == MUL:
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left * right)
            
            elif opcode == DIV:
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(left / right)
            
            elif opcode == STORE:
                var_name = instruction[1]
                value = self.stack.pop()
                self.variables[var_name] = value
            
            elif opcode == LOAD:
                var_name = instruction[1]
                self.stack.append(self.variables[var_name])
            
            elif opcode == HALT:
                break
        
        return self.stack[-1] if self.stack else None