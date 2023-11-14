from crypt import methods
from flask import Flask,make_response,jsonify
from flask_cors import CORS
from WebScrap import list_Banks
from WebScrap.Banco_BAI import BAI
from WebScrap.Banco_BAI_Europa import BAI_Europa
from WebScrap.Banco_BCI import BCI
from WebScrap.Banco_BIC import BIC
from WebScrap.Banco_BNA import BNA
from WebScrap.Banco_StandardBank import StandardBank
from WebScrap.InfoMoney import Infomoney



app = Flask(__name__)

#Permitindo requisições na API
CORS(app)

@app.route('/',methods=["GET"])
def main_paige():
    return make_response(
        jsonify({'API on air!'}))

@app.route('/date/', methods=["GET"])
def d():
    return {'message':'Hello'}

@app.route('/Cambio/', methods=["GET"])
def list_Banks():
    List_Banks = list_Banks
    return {'Banks':List_Banks}    

@app.route('/Cambio/BAI/', methods=["GET"])
def get_Camb_BAI():
    Bai = BAI.Tabela_Cambio
    return Bai

@app.route('/Cambio/BAI_Europa/', methods=["GET"])  
def get_camb_BAI_Europa():
    Bai_Europa = BAI_Europa.Tabela_Cambio
    return Bai_Europa

@app.route('/Cambio/BCI/', methods=["GET"]) 
def get_camb_BCI():
    bci = BCI.Tabela_Cambio
    return bci

@app.route('/Cambio/BIC/', methods=["GET"]) 
def get_camb_BIC():
    bic = BIC.Tabela_Cambio
    return bic

@app.route('/Cambio/StandardBank/', methods=["GET"])  
def get_camb_StandardBank():
    standardbank = StandardBank.Tabela_Cambio
    return standardbank    

@app.route('/Cambio/Infomoney/', methods=["GET"]) 
def get_camb_Infomoney():
    infomoney = Infomoney.Tabela_Cambio
    return infomoney

@app.route('/Cambio/BNA/', methods=["GET"])  
def get_camb_BNA():
    bna = BNA.Tabela_Cambio
    return bna  



app.run()