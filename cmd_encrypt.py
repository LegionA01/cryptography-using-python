import cryptography
from cryptography import fernet

f = cryptography.fernet

n_or_o = input("(N)ew or (O)ld key? ")

if n_or_o.lower() == 'n':
    key = f.Fernet.generate_key()  # generate a new key
    print_key = key.decode('ASCII')  # decode as a string, b/c we want a regular string
    print(print_key)

else:
    key = input("Paste key: \n")
    key = key.encode('ASCII')


def read():
    paste = input("Paste message: \n")
    paste = paste.encode("ASCII")
    paste = f.Fernet(key).decrypt(paste)
    print(paste.decode("ASCII"))


def write():
    message = input("Enter message: \n")
    message = message.encode("ASCII")
    message = f.Fernet(key).encrypt(message)
    print(message.decode("ASCII"))


while True:
    process = input("(R)ead or (W)rite or (Q)uit? \n")
    if process.lower() == 'q':
        break
    elif process.lower() == 'r':
        read()
    elif process.lower() == 'w':
        write()
    else:
        print("Please check entry...")
