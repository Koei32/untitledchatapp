from string import printable

VALID_CHARS = printable[:-6]


def hashit(string):
    return hash(string)


import re


def splitting():
    message = input()
    a = re.split(r"[-;]", message)

    x = a[0] if len(a) > 0 else None
    y = a[1] if len(a) > 1 else None
    z = a[2] if len(a) > 2 else None
    print(f"sender= {x}")
    print(f"receiver= {y}")
    print(f"content= {z}")
    return x, y, z


# splitting()
