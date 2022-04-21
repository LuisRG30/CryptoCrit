import rsa

class KeyGenerator:

    def __init__(self):
        #Create keys
        (pubkey, privkey) = rsa.newkeys(2048)
        self.pubkey = pubkey
        self.privkey = privkey

    def generate_certs(self, cert_priv_location, cert_pub_location):
        #Write public key to file
        cert_pub = cert_pub_location.open("wb")
        cert_pub.write(self.pubkey.save_pkcs1('PEM'))
        cert_pub.close()

        cert_priv = cert_priv_location.open("wb")
        cert_priv.write(self.privkey.save_pkcs1('PEM'))
        cert_priv.close()

    def generate_certs_disk(self):
        with open('publickey.key', 'wb') as f:
            f.write(self.pubkey.save_pkcs1('PEM'))
        with open('privatekey.key', 'wb') as f:
            f.write(self.privkey.save_pkcs1('PEM'))

