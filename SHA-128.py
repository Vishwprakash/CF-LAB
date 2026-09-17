import hashlib

message = input("Enter message: ").encode()

result = hashlib.sha1(message).hexdigest()

print("SHA-1:", result)
