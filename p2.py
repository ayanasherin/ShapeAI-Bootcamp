import hashlib
print(hashlib.algorithms_available)
obj = input("Enter your value: ")
item = obj.encode()
print("sha1 Algorithm: ",hashlib.sha1(item).hexdigest())
print("sha224 Algorithm: ",hashlib.sha224(item).hexdigest())
print("sha256 Algorithm: ",hashlib.sha256(item).hexdigest())

