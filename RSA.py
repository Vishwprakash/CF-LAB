p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

print("Public Key:", e, n)
print("Private Key:", d, n)

m = int(input("Enter message (number < 3233): "))

encrypted = pow(m, e, n)
decrypted = pow(encrypted, d, n)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
