def multiplication_efficient(a, b, mod, p):

    result = 0

    for i in range(p):

        if b & 1:
            result = result ^ a

        b = b >> 1

        if a & (1 << (p - 1)):
            a = (a << 1) ^ mod
        else:
            a = a << 1

    return result


a = int(input("Enter first polynomial in binary: "), 2)
b = int(input("Enter second polynomial in binary: "), 2)
mod = int(input("Enter irreducible polynomial in binary: "), 2)
p = int(input("Enter value of p: "))

result = multiplication_efficient(a, b, mod, p)

print("Multiplication Modulo =", bin(result)[2:])
