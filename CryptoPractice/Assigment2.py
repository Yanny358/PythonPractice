import time
import hashlib

#  MD5
user_entered_password = 'insecurepass'
salt = "somesalty"
db_password = user_entered_password+salt
start_time = time.time()
h = hashlib.md5(db_password.encode())
print(h.hexdigest())
print("--- %s seconds ---" % round(time.time() - start_time, 3))

#  SHA-1
result1 = hashlib.pbkdf2_hmac('sha1', b'insecurepass', b'salt', 100000)  #  The number of iterations should be chosen based on the hash algorithm and computing power. As of 2013, at least 100,000 iterations of SHA-256 are suggested.
print(result1.hex())
print("--- %s seconds ---" % round(time.time() - start_time, 3))

# SHA-256
result256 = hashlib.pbkdf2_hmac('sha256', b'somepass', b'saaaaalt', 100000)
print(result256.hex())
print("--- %s seconds ---" % round(time.time() - start_time, 3))


"""
So MD5 is the fastest and sha256 is slowest
"""