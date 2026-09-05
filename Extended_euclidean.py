def euclidean(a, b):

    while b != 0:
        a, b = b, a % b

    return a

def Ex_euclidean(a,b):
    a,b = max(a,b) , min(a,b)

    q = [-1,-1]
    r = [a,b]
    s = [1,0]
    t = [0,1]

    while r[-1] > 0:
      q.append(r[-2] // r[-1])
      r.append(r[-2] % r[-1])
      s.append(s[-2] - q[-1] * s[-1])
      t.append(t[-2] - q[-1] * t[-1])

    return s[-2] , t[-2]



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", euclidean(a, b))
print(Ex_euclidean(a,b))
