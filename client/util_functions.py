import re
from string import printable

VALID_CHARS = printable[:-6]


# sender-receiver;message
def parse_msg(msg: bytes):
    message = msg.decode()
    x = re.split(r"[-;]", message)

    sender = x[0] if len(x) > 0 else None
    receiver = x[1] if len(x) > 1 else None
    content = x[2] if len(x) > 2 else None

    return sender, receiver, content


# splitting()
