#from tiny import week
from google_images_search import GoogleImagesSearch
from PIL import Image, ImageDraw, ImageFont
from drive import salvar_drive
import io
from io import BytesIO
import requests
#week.to_csv('week.csv',index=False)
def imagem_gen(base_final):
        
    week = base_final
    i = 0
    
    #Formata o NCM
    for n in week['NCM']:
        
        n = '{}.{}.{}'.format(str(n)[:4], str(n)[4:6], str(n)[6:8] )
        week.loc[i,'NCM'] = n
        i = i+1
        
    week.reset_index()
    max_len = len(week.axes[0])

    i = -1
    while i != max_len:
        i = i+1
        if i == max_len:
           
            return(salvar_drive)
            break
 
    
        
        nome_produto = week.loc[i,'Produtos']
        # Configurar a API de busca de imagens do Google
        gis = GoogleImagesSearch('')
        
        # Parâmetros da pesquisa
        search_params = {
            'q': nome_produto,
            'num': 1,  # Número de imagens a serem retornadas
            'safe': 'high',  # Nível de segurança das imagens
        }
        
        # Realizar a pesquisa
        gis.search(search_params)
        
        # Obter a URL da primeira imagem encontrada
        url = gis.results()[0].url
        
        response = requests.get(url)
        # Baixar a imagem
    

        # Carregando a imagem principal
        imagem_principal = Image.open(BytesIO(response.content))
        imagem_tamanho = (1000, 1000)
        imagem_principal = imagem_principal.resize(imagem_tamanho)
        
        # Definir a cor da borda (no exemplo, azul)
        cor_borda = (255, 255, 255)
        
        # Definir a largura da borda (em pixels)
        largura_borda = 300
        
        # Obter as dimensões da imagem original
        largura, altura = imagem_tamanho
        
        # Definir as dimensões da imagem com a borda
        nova_largura = largura + 2 * largura_borda
        nova_altura = altura + 2 * largura_borda
        
        # Criar uma nova imagem com a borda
        imagem_com_borda = Image.new('RGB', (nova_largura, nova_altura),
                                      color=cor_borda)
        
        # Colocar a imagem original dentro da imagem com a borda
        posicao = (largura_borda, largura_borda)
        imagem_com_borda.paste(imagem_principal, posicao)
        
        
        # Carregando a logo
        imagem_principal = imagem_com_borda
        logo = Image.open('C:\VSCODE\imagem\logo.png')
        
        # Definindo o tamanho da logo desejado
        logo_tamanho = (500, 250)
        logo_redimensionada = logo.resize(logo_tamanho)
        
        # Definindo a posição da logo na imagem principal
        posicao_logo = (0, 0)
        
        # Mesclando a imagem principal com a logo
        imagem_final = imagem_principal.copy()
        imagem_final.paste(logo_redimensionada, posicao_logo)
        
        #ALTERA ESCRITA DO BANNER
        # Carregar a imagem
        imagem = Image.open('C:\VSCODE\imagem\eanner.png')
        
        # Criar um objeto de desenho
        desenho = ImageDraw.Draw(imagem)
        
        # Configurar a fonte e tamanho do texto
        fonte = ImageFont.truetype('C:\VSCODE\imagem\eonte.ttf', 40)
        
        # Configurar a posição e o texto desejado
        posicao = (30, 70)
        texto = str(nome_produto)
        
        # Desenhar o texto na imagem
        desenho.text(posicao, texto, fill=(255, 255, 255), font=fonte)
        posicao_logo = (0,1410)
        # Salvar a imagem modificada
    
        imagem_final.paste(imagem, posicao_logo)
        #caminho_imagem = "C:\VSCODE\imagem\P"+ nome_produto +".png" 
        nome_arquivo = 'P'+ str(nome_produto)
        #imagem_final.save(caminho_imagem)
        conteudo_imagem = io.BytesIO()
        imagem_final.save(conteudo_imagem, format='PNG')
        conteudo_imagem.seek(0)
        bytes_imagem = conteudo_imagem.read()
        salvar_drive(bytes_imagem,nome_arquivo,week)

    

    
    
    
    