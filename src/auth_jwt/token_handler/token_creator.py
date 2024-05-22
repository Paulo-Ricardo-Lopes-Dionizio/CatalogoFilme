from datetime import timedelta,datetime
import jwt


class TokenCreator:
    def __init__(self, token_key: str, exp_time_min: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min



    def create(self, uid: int):
        return self.__encode_token(uid)



    def __encode_token(self, uid: int):
        token = jwt.encode({
        'exp': datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN),
        'uid': uid
        }, key=self.__TOKEN_KEY, algorithm='HS256')
        
        return token
    

