from decimal import Decimal


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


p = int(input('Enter the value of p = '))
q = int(input('Enter the value of q = '))
no = int(input('Enter the value of text = '))  # for example H = 8 I = 9
n = p * q  # calculate n
t = (p - 1) * (q - 1)  # calculate totient

for e in range(2, t):  # exponent e
    if gcd(e, t) == 1:
        break

for i in range(1, 10):
    x = 1 + i * t
    if x % e == 0:
        d = int(x / e)  # private key d
        break

ciphertext = Decimal(0)  # for precision
ciphertext = pow(no, e)  # our inputed value to the power of e
ct = ciphertext % n

decryptedtext = Decimal(0)
decryptedtext = pow(ct, d)  # using private key to decrypt message
dt = decryptedtext % n

print('n = '+str(n))
print(' e = '+str(e))
print(' totient = '+str(t))
print(' d = '+str(d))
print('cipher text = '+str(ct))
print(' decrypted text = '+str(dt))
