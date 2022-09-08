import base64
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

def firmar(mensaje):
    with open('ClavePrivada.txt') as file:
        key=file.read()
        rsaKey=RSA.importKey(key)
        signer=Signature_pkcs1_v1_5.new(rsaKey)

        digest=SHA.new()

        digest.update(mensaje)
        print('Contenido del documento\n', mensaje)
        print("Se genero el hash", digest.hexdigest())

        sign=signer.sign(digest)
        signature=base64.b64encode(sign)

    with open('firma.txt', 'wb') as fp1:
        fp1.write(signature)
        fp1.close()
    
    print("Firma creada:", signature)
    print("Firma guardada en: firma.txt")

    return signature

Datos=input('Introduzca el texto a firmar: ')
with open('datos.txt', 'w') as f2:
    f2.write(Datos)

with open("datos.txt", 'r') as f1:
    mensaje=f1.read()

mensaje=mensaje.encode()
signature=firmar(mensaje)


