import rsa

class KeyGenerator:

    def __init__(self):
        #Create keys
        (pubkey, privkey) = rsa.newkeys(2048)
        self.pubkey = pubkey
        self.privkey = privkey

