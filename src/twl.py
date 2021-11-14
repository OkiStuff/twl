from build import Builder
from cli import CLI
from utils import Utils
import sys

from vm import VM


output = "out"

def set_output(name):
    global output
    output = name

def build():
    builder = Builder(contents=Utils.read_file(sys.argv[2]), extension="twlc")

    builder.generate_tokens()
    builder.write_to_binary_file(output)

def run():
    file = open(sys.argv[2], "rb")

    vm = VM(bytes=file.read())
    file.close()

    vm.run()

app = CLI(commands=[["build", "build file", build], ["run", "run compiled file", run]], toggles=[["-o", "--output", "Set output file (for build only)", set_output, True]])

app.parse_toggles()
app.parse()