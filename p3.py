import hashlib
import base64
import uuid
password = input('Enter password :')
pswrd = password.encode()
salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
c = 0
while(c < 5) :
    t_sha = hashlib.sha1()
    t_sha.update(pswrd + salt)
    hashed_password = base64.urlsafe_b64encode(t_sha.digest())
    c = c + 1

print('Hashed value :',hashed_password)
