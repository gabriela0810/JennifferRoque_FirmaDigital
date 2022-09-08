from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

def verificar(mensaje, firma):
    with open('clavePublica.txt') as f:
        key=f.read()
        rsakey=RSA.importKey(key)
        verifier=Signature_pkcs1_v1_5.new(rsakey)
        
        digest=SHA.new()
        digest.update(mensaje)

        print('Calcular Hash de documento recibido', digest.hexdigest())
        print('Desencriptamos la firma para sacar el Hash')

        is_verify=verifier.verify(digest, base64.b64decode(firma))

    if is_verify:
        print('Los Hash coinciden!! \nAutor Legitimo!!')
    else:
        print('Los Hash no son iguales!! \nFirma Ilegal!!')

with open('datos.txt', 'r') as f1:
    mensaje=f1.read()

with open('firma.txt', 'r') as f2:
    firma=f2.read()

mensaje=mensaje.encode()
verificar(mensaje, firma)