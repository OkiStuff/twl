
from utils import Utils


class VM:

    def __init__(self, bytes) -> None:
        self.pc = -1     # For debugging purposes
        self.vsi = 0    # Index on Virtual Stack
        self.stack = [0]
        self.register = 0

        self.bytecode = bytes
        self.jmp_to = -1
    
    def run(self) -> None:
        bytecode = list(self.bytecode)

        for pc in range(lbytecode):
            self.pc += 1
            byte = bytecode[pc]

            if (self.jmp_to >= 0):
                self.jmp_to -= 1
                print(f"Jump To before: {self.jmp_to + 1}\nJump to now: {self.jmp_to}")
                continue

            # Indexing
            if (byte == 0):
                try: self.stack[self.vsi + 1]
                except Exception: self.stack.append(0)
                self.vsi += 1


            elif (byte == 1):
                if (self.vsi > 0): self.vsi -= 1
                else: raise Exception(f"Attempted to set index on Virtual Stack to a negative value\nPC Counter: {self.pc}")

            # Maths
            elif (byte == 2): self.stack[self.vsi] += 1
            elif (byte == 3): self.stack[self.vsi] -= 1
            elif (byte == 4): self.stack[self.vsi] *= self.stack[self.vsi + 1] 
            elif (byte == 5): self.stack[self.vsi] /= self.stack[self.vsi + 1]
            elif (byte == 10): self.stack[self.vsi] -= self.stack[self.vsi + 1]
            elif (byte == 11): self.stack[self.vsi] += self.stack[self.vsi + 1]

            # Piping
            elif (byte == 6): print(self.stack[self.vsi])

            elif (byte == 7):
                stdin = input()
                self.stack[self.vsi] = int(stdin)

            elif (byte == 13):
                i = 0
                while (i < self.stack[self.vsi - 1]):
                    print(self.stack[self.vsi + i], end="")
                    i += 1
                    

            # Element Manipulation
            elif (byte == 8):
                self.stack[self.vsi] = 0

            elif (byte == 9):
                self.stack[self.vsi] = self.stack[self.vsi + 1]
            
            # String
            elif (byte == 12):
                self.stack[self.vsi] = Utils.ascii_values_to_string([self.stack[self.vsi]])

            # Registers
            elif (byte == 14):
                self.stack[self.vsi] = self.register
            
            elif (byte == 15):
                self.register = self.stack[self.vsi]
            
            # XOR
            elif (byte == 16):
                self.stack[self.vsi] = self.stack[self.vsi - 2] ^ self.stack[self.vsi - 1]
            
            # JMP
            elif (byte == 17):
                self.stack[self.vsi] = (self.stack[self.vsi - 2] == self.stack[self.vsi - 3])
                
                if (self.stack[self.vsi] == False):
                    self.jmp_to = self.stack[self.vsi - 1] -