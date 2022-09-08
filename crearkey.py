from Crypto import Random
from Crypto.PublicKey import RSA

random_generator=Random.new().read
rsa=RSA.generate(1024, random_generator)

ClavePrivada=rsa.exportKey()
with open('clavePrivada.txt', 'wb') as f:
    f.write(ClavePrivada)

ClavePublica=rsa.publickey().exportKey()
with open('clavePublica.txt', 'wb') as f:
    f.write(ClavePublica)

print("Se crearon correctamente las llaves")
print("Llave privada\n", ClavePrivada)
print("Llave publica\n", ClavePublica)