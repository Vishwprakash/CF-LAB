n = int(input("Enter number: "))
a = 2

if n <= 1:
    print("Not Prime")
elif pow(a, n - 1, n) == 1:
    print("Probably Prime")
else:
    print("Composite")
