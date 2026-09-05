def multiplication(a, b):

    result = 0

    while a != 0:

        if a & 1:
            result = result ^ b

        a = a >> 1
        b = b << 1

    return result


a = int(input("Enter first polynomial in binary: "), 2)
b = int(input("Enter second polynomial in binary: "), 2)

result = multiplication(a, b)

print("Multiplication =", bin(result)[2:])
