import hashlib

p = 17
a = 2
b = 2

G = (5, 1)
n = 19


def inverse(x):
    return pow(x, -1, p)


def add(P, Q):
    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = ((3 * x1 * x1 + a) * inverse(2 * y1)) % p
    else:
        m = ((y2 - y1) * inverse(x2 - x1)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


def multiply(k, P):
    R = None

    while k > 0:
        if k % 2:
            R = add(R, P)

        P = add(P, P)
        k //= 2

    return R


private_key = 7
public_key = multiply(private_key, G)

message = input("Enter message: ")

h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % n

k = 3

R = multiply(k, G)
r = R[0] % n

k_inv = pow(k, -1, n)
s = (k_inv * (h + private_key * r)) % n

print("Signature:", r, s)
print("Public key:", public_key)
