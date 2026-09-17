import hashlib

message = input("Enter message: ").encode()

result = hashlib.md5(message).hexdigest()

print("MD5:", result)
