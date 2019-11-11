# lets write the basics of a simple data driven machine (CPU simpulation)
# This itteration will just be able to print something
import sys

HALT = 1
PRINT_TOM = 2

# Memory
memory = [
    PRINT_TOM, # [0000 0010]
    PRINT_TOM, # [0000 0010]
    PRINT_TOM, # [0000 0010]
    HALT,      # [0000 0001]
    PRINT_TOM, # [0000 0010]
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
        print("Tom")
    # Decode
    elif command == HALT:
        # Executed
        running = False
    # Decode (error)
    else:
        # Execute
        print(f"Unknown instruction {command}")
        sys.exit(1)

    pc += 1