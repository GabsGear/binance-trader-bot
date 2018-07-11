from Crypto.Cipher import AES
import base64
plain = open("newfile.txt", "r") #query pra pegar do banco
plain = plain.read() #recebe aqui a senha criptografada

binanceKey = "t16ZOkbUCetVG9FZyRl949WRHAYmOSJiBUjVVcanvznZWlzWRfpBa9V8fLfAX5XB"
iv= binanceKey[len(binanceKey) -16:]
key=binanceKey[:32]

AES.key_size=128
crypt_object=AES.new(key=key,mode=AES.MODE_CBC,IV=iv)
decoded=base64.b64decode(plain) 
decrypted=crypt_object.decrypt(decoded)
decrypted=decrypted.decode('utf-8')

print("senha encriptada")
print(plain)
print("senha desencriptada")
print(decrypted)
if(decrypted == "lIQodpmCeu3fAOLpBJvGZJg5ClkB34U4EHJ7d5s09xsSEJc2kylFXXT3w1E2tjAz"):
    print("senha coindice com a original, codificado e decodificado com sucesso")
