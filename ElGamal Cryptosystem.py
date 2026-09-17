p = 23
g = 5

x = int(input("Enter private key: "))
m = int(input("Enter message: "))

y = pow(g, x, p)

k = 3

c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

print("Public key:", y)
print("Encrypted:", c1, c2)

s = pow(c1, x, p)
s_inv = pow(s, -1, p)

decrypted = (c2 * s_inv) % p

print("Decrypted:", decrypted)
