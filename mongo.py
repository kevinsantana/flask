# -*- coding: utf-8 -*-

'''
Registro de um usuario 0 tokens
Cada usuario recebe 10 tokens
Guarda uma frase no banco de dados por 1 token
Recupera a frase guardada no bd por 1 token
'''

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import hashlib

mongo = Flask(__name__)
api = Api(mongo)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]

class Registro(Resource):
    def post(self):
        #passo1: receber os dados do usuario atraves do post
        postedData = request.get_json()
        
        #get data
        username = postedData["username"]
        password = postedData["password"]
        
        #hash (senha)
        hashed_pw = hashlib.sha256(password.encode('utf8')).hexdigest()

        #armazena usuario e senha no banco
        users.insert({
                "Username": username,
                "Password": hashed_pw,
                "Sentence": "",
                "Tokens": 6
        })
    
        retJson = {
                "status": 200,
                "msg": "Cadastro realizado com sucesso"
        }
        return jsonify(retJson)

def verifyPw(username, password):
    hashed_pw_bd = users.find({
            "Username": username
            })[0]["Password"]
    
    #hash da provavel senha
    hashed_pw_test = hashlib.sha256(password.encode('utf8')).hexdigest()
    
    #se a provavel senha for igual ao bd
    if hashed_pw_bd == hashed_pw_test:
        return True
    else:
        return False
    
def countTokens(username):
    tokens = users.find({
            "Username": username
            }) [0]["Tokens"]
    return tokens
    
class Guardar(Resource):
    def post(self):
        #receber post
        postedData = request.get_json()
        
        #ler os dados recebidos
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]
        
        #checar senha
        correct_pw = verifyPw(username, password)
        
        if not correct_pw:
            retJsonm = {
                    "status": 302,
                    "msg": "Senha incorreta"
            }
        return jsonify(retJsonm)
        
        #verificar se possui tokens suficientes
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                    "status": 301,
                    "msg": "Tokens insuficientes"
            }
        return jsonify(retJson)        
        
        #guardar frase e retornar status
        users.update({
                "Username": username
                }, {
                        "$set": {
                                "Sentence": sentence,
                                "Tokens": num_tokens - 1
                                }
                })
            
        retJson = {
                "status": 200,
                "msg": "Frase guardada com sucesso"
        }            
        return jsonify(retJson)

class Get(Resource):
    def post(self):
        postedData = request.get_json()
        
        username = postedData["username"]
        password = postedData["password"]
        
        #checar senha
        correct_pw = verifyPw(username, password)
                
        if not correct_pw:
            retJson = {
                    "status": 302
            }
        return jsonify(retJson)
        
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                    "status": 301
            }
            return jsonify(retJson)
        
        #o usuario deve pagar se ultrapassar a qtd de tokens
        users.update({
                "Username": username
                }, {
                    "$set": {
                    "Tokens": num_tokens - 1
                    }
                })
            
        
        sentence = users.find({
                "Username": username
                })[0]["Sentence"]
        
        retJson = {
                "status": 200,
                "msg": sentence
                }
        
        return jsonify(retJson)       
        

api.add_resource(Registro, '/registrar')
api.add_resource(Guardar, '/guardar')
api.add_resource(Get, '/get')

if __name__== "__main__":
    mongo.run(host = '0.0.0.0')