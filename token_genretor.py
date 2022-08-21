import bcrypt
import jwt


SECRET_KEY = "SHASHONK"


class PasswordSecurity:
    def encryptPassword(password):
        salt = bcrypt.gensalt()
        hashPas = bcrypt.hashpw(password=password,salt=salt)
        return hashPas



class TokenGenretor:
    def __init__(self,username,mailId):
        self.username = username
        self.mailId = mailId


    def encodeToken(self):
        encode = jwt.encode(payload={"username":self.username,"mail":self.mailId},key=SECRET_KEY,algorithm="HS256")
        return encode
    

    def decodeToken(self,token):
        try:
            decode = jwt.decode(jwt=token,key=SECRET_KEY,algorithms="HS256")
            return decode
        except Exception as e:
            return "Error"    


