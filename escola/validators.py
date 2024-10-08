import re

def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    #86 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9{4}]'
    resposta = re.findall(modelo, celular)
    return not resposta # caso não for um celular válido