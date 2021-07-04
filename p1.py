import hashlib

obj = input("Enter your value: ")
item = obj.encode()
print(hashlib.md5(item).hexdigest())
