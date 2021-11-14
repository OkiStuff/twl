
from utils import Utils


class VM:

    def __init__(self, bytes) -> None:
        self.pc = 0     # For debugging purposes
        self.vsi = 0    # Index on Virtual Stack
        self.stack = [0]

        self.bytecode = bytes
    
    def run(self) -> None:
        bytecode = list(self.bytecode)

        for byte in bytecode:
            self.pc += 1

            # Indexing
            if (byte == 0):
                try: self.stack[self.vsi + 1]
                except Exception: self.stack.append(0)
                self.vsi += 1


            elif (byte == 1):
                if (self.vsi > 0): self.vsi -= 1
                else: raise Exception("Attempted to set index on Virtual Stack to a negative value")

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

            # Element Manipulation
            elif (byte == 8):
                self.stack[self.vsi] = 0

            elif (byte == 9):
                self.stack[self.vsi] = self.stack[self.vsi + 1]
            