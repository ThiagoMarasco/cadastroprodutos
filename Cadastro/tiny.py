
import pandas as pd
import requests 
import json
from produtos import produtos
from imagem_gen import imagem_gen
from ncm_cosmos import ncm
from sheets import main
import openai

#base = main()
#base_ncm = ncm(base)
#savez = imagem_gen(base_ncm)


base_week = pd.read_csv('C:\VSCODE\Cadastro\week.csv')
i = -1

max_len = len(base_week.axes[0])

i = -1
while i != max_len:
     i = i+1
     if i == max_len:
         break
     base_week['Preço de Venda'] = base_week['Preço de Venda'].str.replace("R$ ", "").str.replace(",", ".").astype(str)
     base_index = base_week.loc[i]
     ean = base_index['EAN']
     nome = base_index['Produtos']
     ncm_1 = base_index['NCM']
     marca = base_index['Marca']
     anexo1 = base_index['URL']
     preco = base_index['Preço de Venda']

     anexo2 ='https://anexos.tiny.com.br/erp/NjAzNjA0NTA0/min_c7f9efe296bb2c2aa69fafc4dc14d995.png'
     anexo3 ='https://anexos.tiny.com.br/erp/NjAzNjA0NTA0/min_2ccb45bf424e084e66e213f7e1c4766f.png'

    


     openai.api_key = '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'
     

     prompt = nome
     

     objeto = " descrição para venda resumida"
     

     entrada = f"{prompt} {objeto}"

     resposta = openai.Completion.create(
         engine="text-davinci-003",
      prompt=entrada,
         max_tokens=100,
         n=1,
         stop=None,
         temperature=0.7
     )
     

     descricao = resposta.choices[0].text.strip()

     
     url = 'https://api.tiny.com.br/api2/produto.incluir.php/?'
     token = ''


     produto_completo = produtos(nome,int(ean),preco,str(ncm_1),descricao,marca,str(anexo1),str(anexo2),str(anexo3))

     data = url + 'token='+ token + '&produto='+ json.dumps(produto_completo) +"&formato=JSON"
     response = requests.post(data)
     todos = json.loads(response.content)

     print("Resposta:")
     print(todos)
     print(response)