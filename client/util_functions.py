from string import printable
VALID_CHARS = printable[:-6]

def hashit(string):
    return hash(string)


