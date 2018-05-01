#!/usr/bin/env python

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-s[-1]]


class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


cipher = AESCipher('#@protraderbotcriptografia#@')
encrypted = cipher.encrypt('r76Q8Q35KipGTmY4BRuQqx1LDp3fWFvMjGYK9avKZnvbXVAzitWNKupzUtoQ34Uj')
decrypted = cipher.decrypt(encrypted)
print(encrypted)

php = 'Xa/dagrtYtSwQUaHJtfV5V16DEJzJvZTyGJHxjKlgzT5SVuhSGSUqf6UneP/0vEsCDsU1QF8PpvwMe3vm1ReQlgBbBH+UovZ6veI+LgOvi0='

print (php)

if (php == encrypted):
    print (sucess)


