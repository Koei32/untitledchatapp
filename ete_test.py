from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


x = rsa.generate_private_key(key_size=2048, public_exponent=65537)

print(
    x.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.PKCS1
    )
)
print(x)
