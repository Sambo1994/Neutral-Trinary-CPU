import random

class NeutralTrinaryCPU:
    def __init__(self, seed=None):
        """
        Initializes the CPU with registers and a control unit.
        """
        self.registers = {"A": None, "B": None, "C": None}  # Three registers
        self.instruction = None  # Holds current instruction
        if seed is not None:
            random.seed(seed)  # Control randomness for predictability

    def set_register(self, reg, value):
        """
        Sets a register with a value ('0', '1', or '0 or 1').
        """
        if reg in self.registers and value in ['0', '1', '0 or 1']:
            self.registers[reg] = value
        else:
            raise ValueError("Invalid register or value. Allowed values: '0', '1', '0 or 1'.")

    def resolve_state(self, value):
        """
        Resolves an unstable '0 or 1' probabilistically.
        """
        return random.choice(['0', '1']) if value == '0 or 1' else value

    def execute(self, instruction, reg1, reg2=None):
        """
        Executes basic CPU operations.
        Supported operations:
        - 'ADD': Adds reg1 and reg2 (XOR-like logic)
        - 'NOT': Inverts reg1
        """
        if instruction == "ADD" and reg2:
            v1 = self.resolve_state(self.registers[reg1])
            v2 = self.resolve_state(self.registers[reg2])
            self.registers["C"] = str(int(v1) ^ int(v2))  # XOR operation

        elif instruction == "NOT":
            v1 = self.resolve_state(self.registers[reg1])
            self.registers["C"] = '1' if v1 == '0' else '0'

        else:
            raise ValueError("Invalid instruction.")

        return self.registers["C"]  # Result is stored in register C

# Example usage:
if __name__ == "__main__":
    cpu = NeutralTrinaryCPU(seed=42)
    
    # Set register values
    cpu.set_register("A", "0 or 1")
    cpu.set_register("B", "1")

    print("Initial A:", cpu.registers["A"])
    print("Initial B:", cpu.registers["B"])

    # Execute ADD operation (XOR logic)
    result = cpu.execute("ADD", "A", "B")
    print("ADD Result (A XOR B):", result)

    # Execute NOT operation
    result = cpu.execute("NOT", "B")
    print("NOT Result (~B):", result)
