from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

key = b'123456789012345678901234'

plaintext = input("Enter plaintext: ").encode()

cipher = DES3.new(key, DES3.MODE_ECB)

padded_text = pad(plaintext, 8)

ciphertext = cipher.encrypt(padded_text)

print("Encrypted:", ciphertext.hex())

cipher = DES3.new(key, DES3.MODE_ECB)

decrypted = cipher.decrypt(ciphertext)
decrypted = unpad(decrypted, 8)

print("Decrypted:", decrypted.decode())
