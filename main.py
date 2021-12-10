import sys

from repl.repl import Repl

if __name__ == "__main__":
    print()
    print("Welcome to python datalg-REPL")
    print("crtl-c to quit")
    print()
    repl = Repl(sys.stdout)
    repl.loop()
