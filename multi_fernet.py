# cryptography MultiFernet

import cryptography

from cryptography import fernet

f = cryptography.fernet

key1 = f.Fernet(f.Fernet.generate_key())
key2 = f.Fernet(f.Fernet.generate_key())

message = b"This is a hidden flag: CTF{you_know_creeper}"


Multi = f.MultiFernet([key1, key2])

secret = Multi.encrypt(message)  # message is encrypted

print(secret)
