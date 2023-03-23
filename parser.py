from lexer import *
from generate import *


IDENTIFIER = "id"
PIDENTIFIER = "pid"

primitives = [VOID, BOOL, CHAR, BYTE, U8, I8, F8, U16, I16,
              F16, GLYPH, U32, I32, F32, U64, I64, F64, SIZE,
              USIZE, TYPE, NULL ]

operators = [ARROW, ASTERISK, COLON, SLASH, PLUS, MINUS,
             AMPERSAND, VERTICAL_BAR, COMMA, CARET,
             QUESTION_MARK, LOGICAL_NOT]

params = []
i = 0
t = []

class Scope:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.statements = []
        self.definitions = []

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
    curtype = ""
    while t[i][1] not in [EQUAL, SEMICOLON, RIGHT_BRACKET, EOF]:
        curtype += t[i][0]
        i+=1


def parseMain():
    global i, t

def parseIdentifier():
    global i, t
    i+=1
    if t[i][1] == ":":
        i+=1
        parseType()
    elif t[i][1] == "(":
        i+=1
        parseFunc()
    elif t[i][1] == "|>":
        i+=1
        parsePipe()


def parseFunc():
    global i, t
    print("Got func")

def parsePipe():
    global i, t
    print("Got pipe")

def parsePidentifier():
    parseIdentifier()

def parse():
    global i, t
    if t[i][1] == MAIN:
        parseMain()
    if t[i][1] == IDENTIFIER:
        parseIdentifier()
    if t[i][1] == PIDENTIFIER:
        parsePidentifier()
    i+=1
    if(i!=len(t)):
        parse()

if __name__ == "__main__":
    # Read the filename from the command line argument
    if len(sys.argv) != 2:
        print("Usage: python parser.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]

    t = get_tokens(filename)
    parse()
