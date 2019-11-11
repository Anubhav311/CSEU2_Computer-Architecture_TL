# lets continue on from simple01.py
# now we will add 2 byte opcodes so that we can print numbers
import sys

HALT = 1
PRINT_TOM = 2
PRINT_NUM = 3

# Memory
memory = [
    PRINT_TOM, # [0000 0010]
    PRINT_TOM, # [0000 0010]
    PRINT_TOM, # [0000 0010]
    PRINT_NUM,
    45,
    PRINT_TOM, # [0000 0010]
    HALT,      # [0000 0001]
]

# flags

# program counter
pc = 0
# state (running)
running = True

# REPL (FETCH, DECODE, EXECUTE)
while running:
    # Fetch
    command = memory[pc]
    # Decode
    if command == PRINT_TOM:
        # Execute
        instruction_size = 1
        print("Tom")
    # Decode
    elif command == HALT:
        # Executed
        instruction_size = 1
        running = False
    # Decode
    elif command == PRINT_NUM:
        # Execute
        instruction_size = 2
        num = memory[pc + 1]
        print(num)
    # Decode (error)
    else:
        # Execute
        print(f"Unknown instruction {command}")
        sys.exit(1)

    pc += instruction_size