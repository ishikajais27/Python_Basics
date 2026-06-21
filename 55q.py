 #Your Code (High Level Language)
#       ↓
#Interpreter / Compiler
#        ↓
#Bytecode / Machine Code
#        ↓
#Operating System
#        ↓
#CPU executes instructions

# Syntax Errors (Before Running) - happen when Python is converting your code into Python bytecode.

#   Runtime error - error that occurs while the program is running, after the code has started executing.
# Python successfully converts the code and starts execution.occurs after the program has been loaded into memory

#  raise means - I want to create an error myself.
#In general, raise is mostly used inside conditions

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")