import hashlib

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

message = input("Enter message: ")

h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

signature = pow(h, d, n)

print("Signature:", signature)

check = pow(signature, e, n)

if check == h % n:
    print("Signature verified")
else:
    print("Signature not verified")
