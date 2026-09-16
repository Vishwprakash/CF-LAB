from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'

plaintext = input("Enter plaintext: ").encode()

cipher = DES.new(key, DES.MODE_ECB)

padded_text = pad(plaintext, 8)

ciphertext = cipher.encrypt(padded_text)

print("Encrypted:", ciphertext.hex())

cipher = DES.new(key, DES.MODE_ECB)

decrypted = cipher.decrypt(ciphertext)
decrypted = unpad(decrypted, 8)

print("Decrypted:", decrypted.decode())
