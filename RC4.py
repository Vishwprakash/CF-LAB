def RC4(key, text):
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    result = []

    for ch in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        result.append(ch ^ k)

    return bytes(result)


key = input("Enter key: ").encode()
text = input("Enter plaintext: ").encode()

encrypted = RC4(key, text)
print("Encrypted:", encrypted.hex())

decrypted = rc4(key, encrypted)
print("Decrypted:", decrypted.decode())
