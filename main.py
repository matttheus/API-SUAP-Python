# -*- coding: utf-8 -*-
import requests

# Getting the user token
url = 'https://suap.ifrn.edu.br/api/v2/autenticacao/token/'

#username and0 password are parameters of requisition
user_data = {
  'username': '',
  'password': ''
}

requisition = requests.post(url, data=user_data)
if requisition.status_code == requests.codes.ok:
  token_authentication = requisition.json().get('token')
  print ('\n--- Authentication token:\n {} \n\n'.format(token_authentication))

# Getting the user data
url = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'

headers = {
  'Authorization':'JWT {}'.format(token_authentication)
}

requisition = requests.get(url, headers=headers)
if requisition.status_code == requests.codes.ok:
  json_return = requisition.json()
  print ('--- User data:\n{}\n\n'.format(json_return))
