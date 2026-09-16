from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'

plaintext = input("Enter plaintext: ").encode()

cipher = AES.new(key, AES.MODE_ECB)

padded_text = pad(plaintext, 16)

ciphertext = cipher.encrypt(padded_text)

print("Encrypted:", ciphertext.hex())

cipher = AES.new(key, AES.MODE_ECB)

decrypted = cipher.decrypt(ciphertext)
decrypted = unpad(decrypted, 16)

print("Decrypted:", decrypted.decode())
