import sys

__INTERNAL_DEFAULT_HELP_COMMANDS__ = []

def _internal_default_help():
    for i in __INTERNAL_DEFAULT_HELP_COMMANDS__:
        print(f"\t{i[0]}\t-\t{i[1]}")

class CLI:



    def __init__(self, commands = [], toggles = [], help_func = _internal_default_help) -> None:
        self.commands = commands
        self.commands.insert(0, ["help", "Help command", help_func])
        self.toggles = toggles

        global __INTERNAL_DEFAULT_HELP_COMMANDS__
        __INTERNAL_DEFAULT_HELP_COMMANDS__ = self.commands
        

    def get_passed_args(self) -> list:
        buffer = []
        x = 1
        while x < len(sys.argv):
            for y in self.commands:
                # [[command, description, function]]

                if (sys.argv[x] == y[0]): 
                    buffer.append([y[0], y[2]])
                    x += 1

        return buffer

    def parse_toggles(self) -> None:
        x = 1
        while x < len(sys.argv):
            for y in self.toggles:
                # [[toggle_mini, toggle_full, description, function, pass_args]]

                if (sys.argv[x] == y[0] or sys.argv[x] == y[1]):
                    if (y[4]): y[3](sys.argv[x + 1])
                    else: y[3]()
            x += 1

    def parse(self) -> list:
        x = 1
        while x < len(sys.argv):
            for y in self.commands:
                # [[command, description, function]]

                if (sys.argv[x] == y[0]): 
                    y[2]()
                    break

            break

                

            



        