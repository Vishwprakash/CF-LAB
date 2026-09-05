def addition(a, b):
    return a ^ b


a = int(input("Enter first polynomial in binary: "), 2)
b = int(input("Enter second polynomial in binary: "), 2)

result = addition(a, b)

print("Addition =", bin(result)[2:])
