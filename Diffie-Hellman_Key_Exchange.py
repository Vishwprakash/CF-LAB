p = int(input("Enter prime number: "))
g = int(input("Enter primitive root: "))

a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

A = pow(g, a, p)
B = pow(g, b, p)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Public key of A:", A)
print("Public key of B:", B)
print("Shared key of A:", key1)
print("Shared key of B:", key2)
