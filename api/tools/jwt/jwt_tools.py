import jwt
import datetime

class JWT:
    key = "secret"
    
    @classmethod
    def enconde(cls, payload: dict):
        exp_time = int((datetime.datetime.now() + datetime.timedelta(minutes=15)).timestamp())
        claims = {
            "exp" : exp_time
        }
        payload |= claims
        return jwt.encode( payload= payload, key= cls.key)
    
    @classmethod
    def decode(cls, token: str) -> str|None:
        try:
            claims = jwt.decode(jwt= token, key= cls.key, algorithms=["HS256"], options={"verify_exp": False})
            now_time = int(datetime.datetime.now().timestamp())
            if now_time > claims["exp"]:
                return "Token Expired"
        except:
            return 'Invalid Token'


