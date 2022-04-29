import rsa

#Gio because of fírmala Gio
class Gio:

    #To implement keyfile with django (files coming from server)
    def firmala(self, file, keyfile):
        #Open private key file
        data = keyfile.open('rb').read()
        keyfile.close()

        #Load private key
        privkey = rsa.PrivateKey.load_pkcs1(data)

        #Open file and hash
        document = file.open('rb')
        message = document.read()

        #Compute hash
        hash_value = str(rsa.compute_hash(message, 'SHA-512'))

        #Sign the document and save signature with document
        signature = rsa.sign(message, privkey, 'SHA-512')

        return signature, hash_value


    #To implement metadata to detect pulic key to validate against (File coming from user)
    def verificala(self, file, signature_file, keyfile):
        #Open public key file 
        data = keyfile.open('rb').read()
        keyfile.close()

        #Load private key file
        pubkey = rsa.PublicKey.load_pkcs1(data)

        #Open file
        document = file.open('rb')
        message = document.read()

        #Open signature
        signature = signature_file.open('rb').read()

        try:
            rsa.verify(message, signature, pubkey)
            return True
        except:
            return False

    def hashit(self, file):
        #Open file and hash
        document = file.open('rb')
        message = document.read()

        #Compute hash
        hash_value = str(rsa.compute_hash(message, 'SHA-512'))

        return hash_value
