import requests

# Definir a URL de upload do Imgur
url_upload = 'https://api.imgur.com/3/image'

# Definir o cabeçalho da requisição com o seu Client-ID do Imgur
headers = {'Authorization': 'Client-ID'}

# Ler o arquivo de imagem
with open('C:\VSCODE\imagem\logo.png', 'rb') as arquivo:
    # Criar uma requisição POST multipart/form-data com o arquivo
    response = requests.post(url_upload, headers=headers, files={'image': arquivo})

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Obter o link da imagem do JSON de resposta
    link_imagem = response.json()['data']['link']
    print('Imagem enviada com sucesso!')
    print('Link da imagem:', link_imagem)
else:
    print('Erro ao enviar a imagem:', response.status_code)