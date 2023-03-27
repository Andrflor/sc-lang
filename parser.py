from typing import OrderedDict
from lexer import *
from generate import *
import json


IDENTIFIER = "id"
PIDENTIFIER = "pid"

primitives = [VOID, BOOL, CHAR, BYTE, U8, I8, F8, U16, I16,
              F16, GLYPH, U32, I32, F32, U64, I64, F64, SIZE,
              USIZE, TYPE, NULL ]

operators = [ARROW, ASTERISK, COLON]

params = []
i = 0
t = []

class Type:
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to

    def __repr__(self):
        return f"Type(fr={self.fr}, to={self.to})"


    def get_isMapping(self):
        return self.fr != NULL

    def get_isType(self):
        return self.to == TYPE

    def get_isTypeMap(self):
        return self.isType and self.isMapping

    isType = property(get_isType)
    isMapping = property(get_isMapping)
    isTypeMap = property(get_isTypeMap)

class Definition:
    def __init__(self, name, type, value):
        self.type = type
        self.name = name
        self.value = value
        self.scope = cS

class Scope:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.definitions = []

    def push(self, name):
        scope = Scope(name, self)
        self.children.append(scope)
        return scope

    def define(self, definition):
         for _definition in self.definitions:
            if _definition.name == definition.name:
                raise Exception(definition.name + " is already defined in this scope")
            else:
                definition.scope = self
                self.definitions.append(definition)

    def pop(self):
        global cS
        if self.parent == NULL:
            cS = rS
        else:
            cS = self.parent

    def inScope(self, identifier):
        for definition in self.definitions:
            if definition.name == identifier:
                return definition
        if self.parent == NULL:
            return NULL
        else:
            return self.parent.inScope(identifier)

rS = Scope("", NULL)
cS = rS

def parseType():
    global i, t
    type = Type(NULL, OrderedDict())
    j = 1
    lastOperator = ASTERISK
    key = ""
    while t[i][1] != EOF:
        if t[i][1] in primitives:
            if lastOperator == ARROW:
                type = Type(type.to, OrderedDict())
            if key == "":
                type.to[str(j)] = t[i][1]
                j+=1
            else:
                type.to[key] = t[i][1]
                key = ""
            i+=1
            continue
        elif t[i][1] in [IDENTIFIER, PIDENTIFIER]:
            identifier = cS.inScope(t[i][0])
            if t[i+1][1] == COLON:
                key = t[i][0]
                i+=2
                continue
            if identifier == NULL:
                raise Exception("Use of undeclared identifier `" + t[i][0] + "`")
            else:
                if not identifier.isType:
                    raise Exception("Identifier `"+ t[i][0] +  "` is not a defining a type.")
        elif t[i][1] in operators:
            if t[i][1] == COLON:
                if key!= "":
                    raise Exception("Unexpected syntax, colon must be used with name")
            else:
                lastOperator = t[i][1]
        elif t[i][1] in [LEFT_CURLY_BRACE, EQUAL]:
            # TODO: parse actual content and add it to scope
            print(type)
        else:
            raise Exception("Unexpected token `" + t[i][0] + "`")
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
        # parse function arguments
    else:
        if cS.inScope(t[i-1][0]) == NULL:
            raise Exception("Use of undeclared identifier `" + t[i-1][0] + "`")
        else:
            if t[i][1] == PIPE_FORWARD:
                i+=1
                parsePipe()


def parseFunc():
    global i, t

def parsePipe():
    global i, t

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
    try:
        parse()
    except Exception as e:
        print("Error:", e)

