from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from helpers.validacoes import validar_senha

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
      return render_template('login.html')

    if request.method == 'POST':
      email = request.form['email']
      senha = request.form['senha']

      resultado = validar_senha(senha)

      if resultado is True:
        return redirect('/')

      else:
        return render_template('login.html', erros=resultado, email=email)

app.run(host='0.0.0.0', port=8000)
