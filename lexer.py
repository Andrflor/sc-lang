import csv
import sys
from generate import toks, EOF, non_tok_states


all_toks = toks + non_tok_states

def tokMap(token):
    if token == "0":
        return "int"
    if token == "d.":
        return "fl"
    if token in all_toks:
        return token
    else:
        return "id"


# Read in the TSV file and construct the state machine
state_machine = {}
with open('states.tsv', 'r') as f:
    reader = csv.DictReader(f, delimiter='\t', quotechar='\b')
    for row in reader:
        key = row["states"]
        del row["states"]
        state_machine[key] = row



# Define the function to apply the state machine to an input string
def recognize_tokens(input_string):
    tokens = []
    current_state = 'sta'
    string_buffer = ''
    for char in input_string:
        if char == '\t' or ord(char) <= 32:
            char = 'blk'
        elif ord(char) > 126:
            char = 'unc'
        next_state = state_machine[current_state][char]
        if "_--" in next_state:
            string_buffer = ''
            current_state = next_state[:-3]
            continue
        elif "_++" in next_state:
            tokens.append([string_buffer, tokMap(current_state)])
            string_buffer = ''
            current_state = next_state[:-3]
        else:
            current_state = next_state
        if char != "blk":
            string_buffer+=char
    return tokens


def get_tokens(filename):
    # Read in the input file and apply the state machine to recognize the tokens
     with open(filename, 'r') as f:
        input_string = f.read()
        return recognize_tokens(input_string) + [[EOF, EOF]]


if __name__ == "__main__":
    # Read the filename from the command line argument
    if len(sys.argv) != 2:
        print("Usage: python lexer.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]

    tokens = get_tokens(filename)

    # Print out the recognized tokens
    for tok in tokens:
        print(tok[0], tok[1])
