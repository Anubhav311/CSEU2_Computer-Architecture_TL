# lets build up our simulator some more
# now we will add the concept of registers
import sys

HALT = 1
PRINT_TOM = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REG = 5
ADD = 6

# Memory
memory = [
    PRINT_TOM, # [0000 0010]
    SAVE, # save the value 65 to register 2
    65,
    2,
    SAVE, # save the value 20 to register 3
    20,
    3,
    ADD, # ADD the content of register 2 and register 3 
    2,
    3,
    PRINT_REG,
    2,
    HALT,      # [0000 0001]
]

# flags

# program counter
pc = 0

# Registers
register = [0] * 8 # List of 8 registers

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

    # Decode
    elif command == SAVE:
        # Execute
        instruction_size = 3
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num

    # Decode
    elif command == ADD:
        # Execute
        instruction_size = 3
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] =+ register[reg_b]

    # Decode
    elif command == PRINT_REG:
        # Execute
        instruction_size = 2
        reg = memory[pc + 1]
        print(register[reg])

    # Decode (error)
    else:
        # Execute
        print(f"Unknown instruction {command}")
        sys.exit(1)

    pc += instruction_size