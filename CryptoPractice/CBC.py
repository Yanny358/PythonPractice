from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        password = key.encode('utf-8')
        self.key = md5(password).digest()

    def encrypt(self, data):
        vector = get_random_bytes(AES.block_size)
        encryption_cipher = AES.new(self.key, AES.MODE_CBC, vector)
        return vector + encryption_cipher.encrypt(pad(data, AES.block_size))

    def decrypt(self, data):
        file_vector = data[:AES.block_size]
        decryption_cipher = AES.new(self.key, AES.MODE_CBC, file_vector)
        return unpad(decryption_cipher.decrypt(data[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    print(' ENCRYPTION')
    msg = "hello".encode('utf-8')
    pwd = "random"

    encrypted = AESCipher(pwd).encrypt(msg)
    print('Ciphertext:', encrypted)
    print('\n DECRYPTION')
    decrypted = AESCipher(pwd).decrypt(encrypted).decode('utf-8')
    print("Original data: ", msg.decode('utf-8'))
    print("Decrypted data:", decrypted)
    assert msg.decode('utf-8') == decrypted
