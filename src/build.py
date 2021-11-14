from utils import Utils
import struct


class Builder:
    
    class BUILDER_TOKENS_ENUMS:

        """
        [ -     Add one to the index on Virtual Stack
        ] -     Remove one to the index on Virtual Stack
        + -     Add one to the current value on the selected element in the Virtual Stack
        - -     Remove one to the current value on the selected element in the Virtual Stack
        * -     Multiply the current value on the selected element in the Virtual Stack against the value on the next element in the Virtual Stack
        / -     Divide the current value on the selected element in the Virtual Stack against the value on the next element in the Virtual Stack
        > -     Pipe the current value on the selected element in the Virtual Stack to stdout
        < -     Get user input and set it as the current value on the selected element (Numbers only)
        ! -     Clear selected element on Virtual Stack
        ^ -     Set selected element to copy the next element in the Virtual Stack
        { -     Add the next element's value in the Virtual stack to the current element's value in the Virtual Stack
        } -     Subtract the next element's value in the Virtual stack to the current element's value in the Virtual Stack

        { content } -   (NOT IMPLEMENTED) Loop     
        """

        ADD_ONE_INDEX = 0
        SUBTRACT_ONE_INDEX = 1

        ADD_ONE = 2
        SUBTRACT_ONE = 3

        MULTIPLY = 4
        DIVIDE = 5

        PIPE_STDOUT = 6
        PIPE_STDIN = 7
        
        CLEAR_ELEMENT = 8
        COPY_NEXT_ELEMENT = 9

        SUBTRACT_NEXT_ELEMENT = 10
        ADD_NEXT_ELEMENT = 11

    def __init__(self, contents, extension) -> None:
        self.contents : str = contents
        self.tokens = []
        self.extension = extension

    def generate_tokens(self) -> None:
        string = Utils.string_to_array(self.contents)
        x = 0
        for char in string:
            # Indexing

            if (char == '['): self.tokens.append(self.BUILDER_TOKENS_ENUMS.ADD_ONE_INDEX)
            elif (char == ']'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.SUBTRACT_ONE_INDEX)
            
            # Maths
            elif (char == '+'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.ADD_ONE)
            elif (char == '-'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.SUBTRACT_ONE)
            elif (char == '{'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.ADD_NEXT_ELEMENT)
            elif (char == '}'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.SUBTRACT_NEXT_ELEMENT)

            elif (char == '*'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.MULTIPLY)
            elif (char == '/'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.DIVIDE)

            # Piping
            elif (char == '>'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.PIPE_STDOUT)
            elif (char == '<'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.PIPE_STDIN)

            # Element Manipulation
            elif (char == '!'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.CLEAR_ELEMENT)
            elif (char == '^'): self.tokens.append(self.BUILDER_TOKENS_ENUMS.COPY_NEXT_ELEMENT)

    def write_to_binary_file(self, filepath) -> None:
        bytecode = bytearray(self.tokens)

        file = open(f"{filepath}.{self.extension}", "w+b")
        file.write(bytecode)

        file.close()

        if (file.closed != True): raise Exception("File was not able to be properly closed, file should still of been written to.")
