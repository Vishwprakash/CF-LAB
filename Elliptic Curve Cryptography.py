p = 17
a = 2
b = 2

O = None


def inverse(n):
    return pow(n, -1, p)


def add(P, Q):
    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P != Q:
        m = ((y2 - y1) * inverse(x2 - x1)) % p
    else:
        m = ((3 * x1 * x1 + a) * inverse(2 * y1)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


def multiply(k, P):
    R = None

    while k > 0:
        if k % 2 == 1:
            R = add(R, P)

        P = add(P, P)
        k //= 2

    return R


G = (5, 1)

private_key = int(input("Enter private key: "))

public_key = multiply(private_key, G)

print("Base point:", G)
print("Public key:", public_key)
