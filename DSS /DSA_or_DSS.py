import hashlib

p = 23
q = 11
g = 4

x = 3
y = pow(g, x, p)

message = input("Enter message: ")

h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q

k = 7

r = pow(g, k, p) % q
k_inv = pow(k, -1, q)

s = (k_inv * (h + x * r)) % q

print("Signature:", r, s)

w = pow(s, -1, q)

u1 = (h * w) % q
u2 = (r * w) % q

v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

if v == r:
    print("Signature verified")
else:
    print("Signature not verified")
