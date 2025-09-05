import re
from string import printable

VALID_CHARS = printable[:-6]


# sender-receiver;message
def parse_msg(msg: bytes):
    message = msg.decode()
    x = re.split(r"[-;]", message)

    sender = x[0]
    receiver = x[1]
    content = x[2]

    return sender, receiver, content


# splitting()
