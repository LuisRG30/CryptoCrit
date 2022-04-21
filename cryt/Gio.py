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
        hash_value = rsa.compute_hash(document, 'SHA-512')

        #Sign the document and save signature with document
        signature = rsa.sign(document, privkey, 'SHA-512')

        return signature


    #To implement metadata to detect pulic key to validate against (File coming from user)
    def verificala(self, file):
        pass


    def sign(self, file):
        pass