def Ex_euclidean(a, b):
   
    q = [-1, -1]
    r = [a, b]
    s = [1, 0]
    t = [0, 1]

    while r[-1] > 0:
        q.append(r[-2] // r[-1])
        r.append(r[-2] % r[-1])

        s.append(s[-2] - q[-1] * s[-1])
        t.append(t[-2] - q[-1] * t[-1])

    return r[-2], s[-2], t[-2]

def find_inv(a, p):
    gcd, x, y = Ex_euclidean(a, p)
    
    # if gcd is not 1 then inverse does not exist
    if gcd != 1:
        return -1 
        
    # x might be negative, so mod p makes it positive
    return x % p

a = int(input("Enter number n : "))
p = int(input("Enter p: "))

ans = find_inv(a, p)

if ans == -1:
    print("No inverse exists")
else:
    print("Inverse is:", ans)
    
