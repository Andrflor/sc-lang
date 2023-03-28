VOID = "void"
BOOL = "bool"
CHAR = "char"
BYTE = "byte"
U8 = "u8"
I8 = "i8"
F8 = "f8"
U16 = "u16"
I16 = "i16"
F16 = "f16"
GLYPH = "glyph"
U32 = "u32"
I32 = "i32"
F32 = "f32"
U64 = "u64"
I64 = "i64"
F64 = "f64"
SIZE = "size"
USIZE = "usize"
TYPE = "type"
NULL = "null"
SEMICOLON = ";"
PIPE_FORWARD = "|>"
ARROW = "->"
ASTERISK = "*"
SLASH = "/"
PLUS = "+"
MINUS = "-"
AMPERSAND = "&"
LOGICAL_AND = "&&"
COLON = ":"
LOGICAL_OR = "||"
DOUBLE_SLASH = "//"
COMMENT_START = "/*"
COMMENT_END = "*/"
TILDE_SLASH = "~/"
TILDE_EQUAL = "~="
DOUBLE_RIGHT_SHIFT = ">>"
RIGHT_SHIFT_EQUAL = ">>="
DOUBLE_LEFT_SHIFT = "<<"
LEFT_SHIFT_EQUAL = "<<="
TILDE = "~"
BITWISE_XOR = "~|"
BITWISE_XOR_EQUAL = "~|="
VERTICAL_BAR = "|"
COMMA = ","
CARET = "^"
CARET_EQUAL = "^="
QUESTION_MARK = "?"
PERCENT = "%"
DOUBLE_QUESTION_MARK = "??"
DOUBLE_QUESTION_MARK_EQUAL = "??="
NOT_EQUAL = "!="
INCREMENT = "++"
DECREMENT = "--"
PLUS_EQUAL = "+="
MINUS_EQUAL = "-="
ASTERISK_EQUAL = "*="
SLASH_EQUAL = "/="
TILDE_SLASH_EQUAL = "~/="
PERCENT_EQUAL = "%="
EQUAL = "="
LOGICAL_NOT = "!"
DOUBLE_LOGICAL_NOT = "!!"
NOT_NULL_ASSERTION = "!."
OPTIONAL_CHAINING = "?."
BANG_NOT_NULL_ASSERTION = "?!."
NOT_BANG_OPTIONAL_CHAINING = "!?."
RETURN_ON_ERROR = "!@"
RETURN_ON_NULL = "?@"
RETURN_ON_ERROR_OR_NULL = "!?@"
RETURN_ON_NULL_OR_ERRROR = "?!@"
PANIC_ON_ERROR = "!#"
PANIC_ON_NULL = "?#"
PANIC_ON_ERROR_OR_NULL = "!?#"
PANIC_ON_NULL_OR_ERRROR = "?!#"
LESS_THAN = "<"
LESS_THAN_OR_EQUAL = "<="
GREATER_THAN_OR_EQUAL = ">="
GREATER_THAN = ">"
EQUAL_EQUAL = "=="
NOT_EQUAL = "!="
ELLIPSIS = "..."
RANGE = ".."
RANGE_EQUAL = "..="
DOT = "."
DOUBLE_QUOTE = "\""
SINGLE_QUOTE = "'"
DOLLAR = "$"
UNDERSCORE = "_"
HASH = "#"
AT = "@"
LEFT_BRACKET = "["
RIGHT_BRACKET = "]"
LEFT_PARENTHESIS = "("
RIGHT_PARENTHESIS = ")"
LEFT_CURLY_BRACE = "{"
RIGHT_CURLY_BRACE = "}"
FOR = "for"
WHILE = "while"
DO = "do"
IF = "if"
ELSE = "else"
IN = "in"
SWITCH = "switch"
DEFAULT = "default"
BREAK = "break"
CONTINUE = "continue"
CASE = "case"
MATCH = "match"
IMPORT = "import"
MUT = "mut"
RETURN = "return"
EOF = "EOF"

SPACE = 32

toks = [VOID, BOOL, CHAR, BYTE, U8, I8, F8, U16, I16, F16, GLYPH, U32, I32,
        F32, U64, I64, F64, SIZE, USIZE, TYPE, NULL, SEMICOLON, PIPE_FORWARD,
        ARROW, ASTERISK, SLASH, PLUS, MINUS, AMPERSAND, LOGICAL_AND, COLON,
        LOGICAL_OR, DOUBLE_SLASH, COMMENT_START, COMMENT_END, TILDE_SLASH,
        TILDE_EQUAL, DOUBLE_RIGHT_SHIFT, RIGHT_SHIFT_EQUAL, DOUBLE_LEFT_SHIFT,
        LEFT_SHIFT_EQUAL, TILDE, BITWISE_XOR, BITWISE_XOR_EQUAL, VERTICAL_BAR,
        COMMA, CARET, CARET_EQUAL, QUESTION_MARK, PERCENT,
        DOUBLE_QUESTION_MARK, DOUBLE_QUESTION_MARK_EQUAL, NOT_EQUAL, INCREMENT,
        DECREMENT, PLUS_EQUAL, MINUS_EQUAL, ASTERISK_EQUAL, SLASH_EQUAL,
        TILDE_SLASH_EQUAL, PERCENT_EQUAL, EQUAL, LOGICAL_NOT,
        DOUBLE_LOGICAL_NOT, NOT_NULL_ASSERTION, OPTIONAL_CHAINING,
        BANG_NOT_NULL_ASSERTION, NOT_BANG_OPTIONAL_CHAINING, RETURN_ON_ERROR,
        RETURN_ON_NULL, RETURN_ON_ERROR_OR_NULL, RETURN_ON_NULL_OR_ERRROR,
        PANIC_ON_ERROR, PANIC_ON_NULL, PANIC_ON_ERROR_OR_NULL,
        PANIC_ON_NULL_OR_ERRROR, LESS_THAN, LESS_THAN_OR_EQUAL,
        GREATER_THAN_OR_EQUAL, GREATER_THAN, EQUAL_EQUAL, NOT_EQUAL, ELLIPSIS,
        RANGE, DOT, DOUBLE_QUOTE, SINGLE_QUOTE, DOLLAR, UNDERSCORE, HASH, AT,
        LEFT_BRACKET, RIGHT_BRACKET, LEFT_PARENTHESIS, RIGHT_PARENTHESIS,
        LEFT_CURLY_BRACE, RIGHT_CURLY_BRACE, FOR, WHILE, DO, IF, ELSE, IN,
        SWITCH, DEFAULT, BREAK, CONTINUE, CASE, MATCH, IMPORT, MUT, RETURN]

non_tok_states = ["sta", "id", "pid", "fl", "int", "hex", "oct",
                  "bin", "unc", "0", "d.", "ch", "str"]

ascii = ["blk"] + [chr(i) for i in range(33, 127)] + ["unc"]


def newRow():
    return dict.fromkeys(ascii, "")


def generateStates():
    states = []
    for tok in toks:
        for i in range(len(tok)):
            states.append(tok[0:i+1])
    return list(set(states))


dlt = {}
# TODO: handle unc
if __name__ == "__main__":
    tok_states = generateStates()
    states = tok_states + non_tok_states
    alnum = [state for state in tok_states if state.isalnum()]
    onestate = [state for state in states if len(state) == 1]
    onechar = [state for state in onestate if state.isalnum()]
    onsymb = [state for state in onestate if not state.isalnum()]
    for state in states:
        dlt[state] = newRow()
    dlt["sta"]["blk"] = "sta_--"
    dlt["sta"]["unc"] = "unc"
    for state in onestate:
        dlt["sta"][state] = state
    for elt in dlt["sta"]:
        if dlt["sta"][elt] == "":
            if elt.isalpha():
                dlt["sta"][elt] = "id"
            elif elt.isnumeric():
                dlt["sta"][elt] = "int"
            else:
                dlt["sta"][elt] = "sta_--"
    dlt["id"]["blk"] = "sta_++"
    dlt["id"]["`"] = "sta_++"
    dlt["id"]["\\"] = "sta_++"
    dlt["id"]["unc"] = "unc"
    for elt in onsymb:
        dlt["id"][elt] = elt + "_++"
    dlt["id"]["_"] = "id"
    for elt in dlt["id"]:
        if dlt["id"][elt] == "":
            dlt["id"][elt] = "id"
    for elt in dlt["pid"]:
        if dlt["id"][elt] == "id":
            dlt["pid"][elt] = "pid"
        else:
            dlt["pid"][elt] = dlt["id"][elt]
        dlt["_"][elt] = dlt["pid"]
    for elt in dlt["0"]:
        if elt == "b":
            dlt["0"][elt] = "bin"
        elif elt == "x":
            dlt["0"][elt] = "hex"
        elif elt == "o":
            dlt["0"][elt] = "oct"
        elif elt == "blk" or elt == "`" or elt == '\\':
            dlt["0"][elt] = "sta_++"
        elif elt == "unc":
            dlt["0"][elt] = "unc"
        elif elt.isalpha() or elt == "_":
            dlt["0"][elt] = "id"
        elif elt.isnumeric():
            dlt["0"][elt] = "int"
        elif elt == ".":
            dlt["0"][elt] = "d."
        else:
            dlt["0"][elt] = elt + "_++"
    for elt in dlt["int"]:
        if elt == "blk" or elt == "`" or elt == '\\':
            dlt["int"][elt] = "sta_++"
        elif elt == "unc":
            dlt["int"][elt] = "unc"
        elif elt.isalpha() or elt == "_":
            dlt["int"][elt] = "id"
        elif elt.isnumeric():
            dlt["int"][elt] = "int"
        elif elt == ".":
            dlt["int"][elt] = "d."
        else:
            dlt["int"][elt] = elt + "_++"
    for elt in dlt["d."]:
        if elt == "blk" or elt == "`" or elt == '\\':
            dlt["d."][elt] = "sta_++"
        elif elt == "unc":
            dlt["d."][elt] = "unc"
        elif elt.isalpha() or elt == "_":
            dlt["d."][elt] = "id_++"
        elif elt.isnumeric():
            dlt["d."][elt] = "fl"
        elif elt == ".":
            dlt["d."][elt] = ".._-+"
        else:
            dlt["d."][elt] = elt + "_++"
    for elt in dlt["fl"]:
        if elt == "blk" or elt == "`" or elt == '\\':
            dlt["fl"][elt] = "sta_++"
        elif elt == "unc":
            dlt["fl"][elt] = "unc"
        elif elt.isalpha() or elt == "_":
            dlt["fl"][elt] = "id_++"
        elif elt.isnumeric():
            dlt["fl"][elt] = "fl"
        else:
            dlt["fl"][elt] = elt + "_++"
    for elt in dlt["bin"]:
        if elt == "0" or elt == "1":
            dlt["bin"][elt] = "bin"
        elif elt == "blk" or elt == "`" or elt == '\\':
            dlt["bin"][elt] = "sta_++"
        elif elt == "unc":
            dlt["bin"][elt] = "unc"
        elif elt.isalnum() or elt == "_":
            dlt["bin"][elt] = "id"
        else:
            dlt["bin"][elt] = elt + "_++"
    for elt in dlt["oct"]:
        if elt == "0" or elt == "1" or elt == "2" or elt == "3" or elt == "4" or elt == "5" or elt == "6" or elt == "7":
            dlt["oct"][elt] = "oct"
        elif elt == "blk" or elt == "`" or elt == '\\':
            dlt["oct"][elt] = "sta_++"
        elif elt == "unc":
            dlt["oct"][elt] = "unc"
        elif elt.isalnum() or elt == "_":
            dlt["oct"][elt] = "id"
        else:
            dlt["oct"][elt] = elt + "_++"
    for elt in dlt["hex"]:
        if elt.isnumeric() or elt == "a" or elt == "b" or elt == "c" or elt == "d" or elt == "e" or elt == "f" or elt == "A" or elt == "B" or elt == "C" or elt == "D" or elt == "E" or elt == "F":
            dlt["hex"][elt] = "hex"
        elif elt == "blk" or elt == "`" or elt == '\\':
            dlt["hex"][elt] = "sta_++"
        elif elt == "unc":
            dlt["hex"][elt] = "unc"
        elif elt.isalnum() or elt == "_":
            dlt["hex"][elt] = "id"
        else:
            dlt["hex"][elt] = elt + "_++"
    for state in tok_states:
        if state == "\"" and state == "'":
            for elt in dlt[state]:
                if elt == '\\':
                    pass
                elif elt == "$":
                    pass
                elif elt == state:
                    dlt[state][elt] = "sta_++"
                else:
                    dlt[state][elt] = "ch"
        elif state.isalnum():
            for elt in dlt[state]:
                if state + elt in tok_states:
                    dlt[state][elt] = state+elt
                elif elt == "blk" or elt == "`" or elt == '\\':
                    dlt[state][elt] = "sta_++"
                elif elt == "unc":
                    dlt[state][elt] = "unc"
                elif elt.isalnum():
                    dlt[state][elt] = "id"
                else:
                    dlt[state][elt] = elt + "_++"
        else:
            for elt in dlt[state]:
                if state + elt in tok_states:
                    dlt[state][elt] = state+elt
                elif elt == "0":
                    dlt[state][elt] = "0_++"
                elif elt == "blk" or elt == "`" or elt == '\\':
                    dlt[state][elt] = "sta_++"
                elif elt == "unc":
                    dlt[state][elt] = "unc"
                elif elt in onestate:
                    dlt[state][elt] = elt + "_++"
                elif elt.isnumeric():
                    dlt[state][elt] = "int_++"
                elif elt.isalpha():
                    dlt[state][elt] = "id_++"
                else:
                    dlt[state][elt] = elt + "_++"
    data = "states"
    for e in dlt["sta"]:
        data += "\t" + e
    for elt in dlt:
        data += "\n" + elt
        for e in dlt[elt]:
            data += "\t" + dlt[elt][e]
    print(data)
