import jwt

class JWT_Manager:
    def __init__(self):
        with open("private.pem", "rb") as f:
            self.private = f.read()
        with open("public.pem", "rb") as f:
            self.public = f.read()

        self.algorithm = "RS256"

    def encode(self, data):
        try:
            return jwt.encode(data, self.private, algorithm=self.algorithm)
        except Exception as e:
            print("Error en encode:", e)
            return None
    
    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public, algorithms=[self.algorithm])
            print("Decoded JWT:", decoded)
            return decoded
        except Exception as e:
            print(e)
            return None