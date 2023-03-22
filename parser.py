from lexer import *
from generate import *


IDENTIFIER = "id"
PIDENTIFIER = "pid"

params = []
i = 0
t = []

class Scope:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.statements = []

    def push(self, name):
        scope = Scope(name, self)
        self.children.append(scope)
        return scope

    def add(self, statement):
        statement.scope = self
        self.statements.append(statement)
        return statement


rS = Scope("", NULL)

def parseType():
    global i, t


def parseMain():
    global i, t

def parseIdentifier():
    global i, t
    i+=1
    if t[i] == ":":
        i+=1
        parseType()

def parsePidentifier():
    global i, t

def parse():
    global i, t
    if t[i][1] == MAIN:
        parseMain()
    if t[i][1] == IDENTIFIER:
        parseIdentifier()
    if t[i][1] == PIDENTIFIER:
        parsePidentifier()

if __name__ == "__main__":
    # Read the filename from the command line argument
    if len(sys.argv) != 2:
        print("Usage: python parser.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]

    t = get_tokens(filename)
    parse()
