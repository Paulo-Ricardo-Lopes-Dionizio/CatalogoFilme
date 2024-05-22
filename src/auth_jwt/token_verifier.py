from flask import request, jsonify
from .token_handler import token_creator
import jwt

def token_verify(function: callable) -> callable:
    def decorated(*arg, **kwargs):
        raw_token = request.headers.get("Authorization")
        uid = request.headers.get("uid")

        if not raw_token or not uid:
            return jsonify({
                'error': 'Não Autorizado!'
            }), 400
        
        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(token, key='secretKey', algorithms="HS256")
            token_uid = token_information["uid"]
        except jwt.InvalidSignatureError:
            return jsonify({
                'error': "Token Inválido!"
            }), 401
        except jwt.ExpiredSignatureError:
            return jsonify({
                'error': "Token Expirado!"
            }), 401
        except KeyError as e:
            return jsonify({
                'error': "Token Inválido!"
            }), 401
        
        if int(token_uid) != int(uid):
            return jsonify({
                'error': "Usuário não permitido!"
            }), 400
    
    return decorated