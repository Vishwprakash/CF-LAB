import hmac
import hashlib

key = input("Enter key: ").encode()
message = input("Enter message: ").encode()

result = hmac.new(key, message, hashlib.sha256)

print("HMAC:", result.hexdigest())
