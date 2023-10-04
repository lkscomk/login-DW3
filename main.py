from flask import Flask, render_template, request, redirect, url_for
from helpers.validacoes import validar_senha

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
      return render_template('cadastro.html')
    
    if request.method == 'POST':
      nomeCompleto = request.form['nomeCompleto']
      cpf = request.form['cpf']
      email = request.form['email']
      telefone = request.form['telefone']
      endereco = request.form['endereco']
      senha = request.form['senha']

      confirmarSenha = request.form['confirmarSenha']

      resultado = validar_senha(senha)

      if senha != confirmarSenha:
        resultado.append('As senhas devem ser iguais')

      if resultado is True:
        return redirect('/')

      else:
        return render_template('cadastro.html', erros=resultado, nomeCompleto=nomeCompleto, cpf=cpf, telefone=telefone, endereco=endereco, email=email)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
      return render_template('login.html')

    if request.method == 'POST':
        return redirect('/')

app.run(host='0.0.0.0', port=8000)
