from typing import Type


try: 
    while(1):
        x = input(">> ")
        code = str()
        try:
            for i in range(0, ord(x)): code += "+" 
        except TypeError: print("Syntax Error, expected only 1 character", end="")
        print(code)
except KeyboardInterrupt: pass