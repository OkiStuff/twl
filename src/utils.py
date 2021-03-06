import sys


class Utils:

    def read_file(filename : str) -> str:
        file = open(filename, 'r')
        buf = file.read()

        file.close()

        if (file.closed != True): raise Exception("File was not able to be properly closed.")

        return buf



    def string_to_array(string : str) -> list:
        return [c for c in string]

    def ascii_values_to_string(values : list) -> str:
        buf : str = ""
        for i in values: buf += chr(i)
        return buf