def multiply_mod(a, b, modulus):

    product = 0

    while a > 0:

        if a % 2 == 1:
            product = product ^ b

        a = a // 2
        b = b << 1

    while product.bit_length() >= modulus.bit_length():

        difference = product.bit_length() - modulus.bit_length()

        product = product ^ (modulus << difference)

    return product


a = int(input("Enter first polynomial in binary: "), 2)
b = int(input("Enter second polynomial in binary: "), 2)
modulus = int(input("Enter irreducible polynomial in binary: "), 2)

answer = multiply_mod(a, b, modulus)

print("Result =", bin(answer)[2:])
