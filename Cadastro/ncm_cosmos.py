
import json
import urllib.request as urllib2

def ncm(base_dados):
     #cest = pd.read_excel("C:\VSCODE\Cadastro\json\CEST.xlsx")
     
     headers = {
               'X-Cosmos-Token': '',
               'Content-Type': 'application/json',
               'User-Agent': 'Cosmos-API-Request'
      }
     
     week = base_dados
     week = week.loc[1:]
     week = week.loc[week['EAN']!='']
     week = week.reset_index()
     week = week.dropna(subset=["EAN"])
     ean = week.loc[0:,"EAN"]
     
     
     i = -1
     for n in ean:
          i = i + 1
          req = urllib2.Request('https://api.cosmos.bluesoft.com.br/gtins/'+str(n)+'.json',None,headers)
          response = urllib2.urlopen(req)
          data_cosmos = json.loads(response.read())
          ncm = data_cosmos["ncm"]
          ncm_code = ncm['code']
          week.loc[i,'NCM'] = ncm_code

     
     return(week)

