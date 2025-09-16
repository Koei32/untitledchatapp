import re
from string import printable, ascii_letters, digits

VALID_CHARS = printable[:-6]
VALID_USR_CHARS = ascii_letters + "_" + digits


# sender-receiver;message
def parse_msg(msg: bytes):
    message = msg.decode()
    x = re.split(r"[-;]", message)

    sender = x[0]
    receiver = x[1]
    content = x[2]

    return sender, receiver, content
