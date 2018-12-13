# -*- coding: utf-8 -*-
import requests

# Obtendo o token do usuário.
url = 'https://suap.ifrn.edu.br/api/v2/autenticacao/token/'

#username e o password são os seus dados utilizads para acessar o SUAP
dados_usuario = {
  'username': '',
  'password': ''
}

requisicao = requests.post(url, data=dados_usuario)
if requisicao.status_code == requests.codes.ok:
  token_autenticacao = requisicao.json().get('token')
  print ('\n--- Token de Autenticação:\n {} \n\n'.format(token_autenticacao))

# Obtendo os dados do usuário.
url = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'
headers = {
  'Authorization':'JWT {}'.format(token_autenticacao)
}
requisicao = requests.get(url, headers=headers)
if requisicao.status_code == requests.codes.ok:
  retorno_json = requisicao.json()
  print ('--- Dados do Usuário Logado:\n{}\n\n'.format(retorno_json))
