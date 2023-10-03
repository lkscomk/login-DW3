#nesse arquivo deve ficar validações, de obrigatoriedade, tamanho, datas, idade
#as funcao desse aquivo devem ser importandas sempre que precisar

import re

def validar_senha(senha):
    erros = []
    if len(senha) < 6:
        erros.append('A Senha deve ser maior que ou igual a 6 digitos.')
    if not re.search(r'[A-Z]', senha):
        erros.append('A Senha deve ter pelo menos UMA letra maiuscula.')
    if not re.search(r'[a-z]', senha):
        erros.append('A Senha deve ter pelo menos UMA letra minuscula.')
    if not re.search(r'\d', senha):
        erros.append('A Senha deve ter pelo menos UM número.')
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]', senha):
        erros.append('A Senha deve ter pelo menos UM caracter especial')
    return True if len(erros) <= 0 else erros
