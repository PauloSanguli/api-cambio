from flask import Flask
from flask import make_response
from flask import jsonify
from flask_cors import CORS
from ScanPDF import  Scaning
from WebScrap import ListMoedas
from WebScrap.Banco_BAI import BAI
from WebScrap.Banco_BAI_Europa import BAI_Europa
from WebScrap.Banco_BIC import BIC
from WebScrap.Banco_BCI import BCI
from WebScrap.Banco_StandardBank import StandardBank
from WebScrap.InfoMoney import Infomoney
from WebScrap.Banco_BNA import BNA


app = Flask(__name__)
CORS(app)

@app.route('/',methods=["GET"])
def Main():
    return make_response(
        jsonify({'SMS':'API on air'})
    )

@app.route('/Moedas/',methods=["GET"])
def Moedas():
    moedas = ListMoedas()
    return make_response(
        jsonify(moedas.self)
    )    

@app.route('/Data/',methods=["GET"])
def DAta():
    data_camb = StandardBank()
    return make_response(
        jsonify(data_camb.data)
    )   

@app.route('/Cambio/BAI/', methods=["GET"])
def baI():
    bai = BAI()
    return make_response(
        jsonify(bai.Tabela_Cambio)
    )

@app.route('/Cambio/StandardBank/', methods=["GET"])
def standardBanK():
    standardbank = StandardBank()
    return make_response(
        jsonify(standardbank.Tabela_Cambio)
    )

@app.route('/Cambio/BCI/', methods=["GET"])
def bcI():
    bci = BCI()
    return make_response(
        jsonify(bci.Tabela_Cambio)
    )

@app.route('/Cambio/BIC/', methods=["GET"])
def biC():
    bic = BIC()
    return make_response(
        jsonify(bic.Tabela_Cambio)
    )

@app.route('/Cambio/Infomoney/', methods=["GET"])
def infomoneY():
    infomoney = Infomoney()
    return make_response(
        jsonify(infomoney.Tabela_Cambio)
    )    

@app.route('/Cambio/BNA/', methods=["GET"])
def bnA():
    bna = BNA()
    return make_response(
        jsonify(bna.Tabela_Cambio)
    )    

@app.route('/Cambio/BAI_Europa/', methods=["GET"])
def bai_europA():
    bai_europa = BAI_Europa()
    return make_response(
        jsonify(bai_europa.Tabela_Cambio)
    )        

@app.route('/Convert/values/', methods=["GET"])
def send_values_convert():
    values = [
        StandardBank.Tabela_Cambio[17]['venda'],StandardBank.Tabela_Cambio[11]['venda'],125
    ]
    return make_response(
        jsonify(values)
    )

@app.route('/Impostos/', methods=['GET'])
def send_imposto():
    pages = Scaning.text_pages
    return make_response(
        jsonify(pages)
    )

app.run(debug=True)