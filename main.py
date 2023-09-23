from flask import Flask, render_template, make_response, request
from calcular_imc import calcular_IMC, interpretar_IMC
from db import db

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('index.html', imc= None, interpretacao=None, error=None)

@app.route('/', methods=['POST'])
def coletar_dados():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    peso = request.form.get('peso')
    altura = request.form.get('altura')


    if peso is None or altura is None:
        response = make_response(render_template('index.html',error="Peso e altura são campos obrigatórios"), 400)
    else:
        try:
            nome = str(nome)
            telefone = str(telefone)
            peso = float(peso)
            altura = float(altura)
            
        except ValueError:
            response = make_response(render_template ('index.html' , error="Peso e altura devem ser números válidos"), 400)
        else:
            if peso <= 0 or altura <= 0:
                response = make_response(render_template('index.html', error="Peso e altura devem ser valores positivos"), 400)
            else:
                
                imc = calcular_IMC(peso, altura)
                format_imc = (format(imc, '.2f'))
                interpretacao = interpretar_IMC(imc)
                peso = str(peso)
                altura = str(altura)
                dados = {
                    'nome': nome,
                    'peso':peso,
                    'altura':altura,
                    'interpretacao':interpretacao,
                    'imc':format_imc,
                    'telefone':telefone
                }
                response = make_response(render_template('index.html', imc=format_imc, interpretacao=interpretacao, nome=nome), 200)
                colecao = db['dados_imc']
                colecao.insert_one(dados)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
    