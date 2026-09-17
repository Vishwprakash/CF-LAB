import hashlib

p = 23
g = 5

a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

password = input("Enter shared password: ")

A = pow(g, a, p)
B = pow(g, b, p)

keyA = pow(B, a, p)
keyB = pow(A, b, p)

checkA = hashlib.sha256((str(keyA) + password).encode()).hexdigest()
checkB = hashlib.sha256((str(keyB) + password).encode()).hexdigest()

print("Public key A:", A)
print("Public key B:", B)

if checkA == checkB:
    print("Authentication successful")
    print("Shared key:", keyA)
else:
    print("Authentication failed")
