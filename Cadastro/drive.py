import requests

def salvar_drive(caminho_png,nome_arquivo,week):



    # Definir a URL de upload do Imgur
    url_upload = 'https://api.imgur.com/3/image'
    
    # Definir o cabeçalho da requisição com o seu Client-ID do Imgur
    headers = {'Authorization': 'Client-ID '}
    
    # Ler o arquivo de imagem

    
        # Criar uma requisição POST multipart/form-data com o arquivo
    response = requests.post(url_upload, headers=headers, files={'image': caminho_png})

    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obter o link da imagem do JSON de resposta
        link_imagem = response.json()['data']['link']
        print('Imagem enviada com sucesso!')
        print('Link da imagem:', link_imagem)
    else:
        print('Erro ao enviar a imagem:', response.status_code)
    
   
    nome_png = nome_arquivo
    nome_png = '{}'.format(str(nome_png)[1:])
    rename = week.index[(week['Produtos'] == nome_png)].tolist()
    week.loc[rename,'URL'] = link_imagem
    print(week)


    week.to_csv('C:\VSCODE\Cadastro\week.csv',index=False)
    print("imagens baixou")
    return(week)




    # Imprimir os IDs e nomes dos arquivos
    