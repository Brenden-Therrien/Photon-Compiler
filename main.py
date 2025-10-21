# main file where we run shit

import lexer
import parser
import compiler
import vm
from opcodes import *

def run_photon(code):
    """
    Complete pipeline:
    code → tokens → AST → bytecode → execution
    """
    
    # Step 1: Lexer - tokenize the code
    print("=== LEXING ===")
    tokens = lexer.tokenize(code)
    print(f"Tokens: {tokens}\n")
    
    # Step 2: Parser - build AST
    print("=== PARSING ===")
    parser.tokens = tokens
    parser.position = 0
    parser.current_token = tokens[0] if tokens else None
    
    # For now, just parse one var declaration
    ast = parser.parse_var_declaration()
    print(f"AST: {ast}\n")
    
    # Compiler - generate bytecode
    print("=== COMPILING ===")
    bytecode = compiler.compile_var_declaration(ast)
    print(f"Bytecode: {bytecode}\n")
    
    # Step 4: VM - execute bytecode
    print("=== EXECUTING ===")
    virtual_machine = vm.VM()
    result = virtual_machine.execute(bytecode)
    print(f"Result: {result}")
    print(f"Variables: {virtual_machine.variables}\n")


if __name__ == "__main__":
    # Test it!
    code = "var x int = 5 + 3 * 2"
    run_photon(code)