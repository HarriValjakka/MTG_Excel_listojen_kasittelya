import pandas as pd
import requests

#Rullattavien sivujen määrä + 1
Number_Of_Pages = 212
headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

#Filtteröidään pandas:sin avulla taulukot sivuston tekstistä
#Sivustolla kaksi taulukkoa, joista jälkimmäinen kiinnostaa
URL = "https://poromagia.com/credit/?set=any&want=ALL&min_price=&color=any"
r = requests.get(URL, headers=headers)
file = r.content
table = pd.read_html(file)
dataFrames = {}
dataFrames["df{0}".format(1)] = table[1]
print(table[1])
print ('First Table')


#Tehdään sama kuin ylhäällä mutta looppina kaikille lopuille halutuille URL:leille
x=2
for x in range (2, Number_Of_Pages):
   URL = "https://poromagia.com/credit/?page={}&want=ALL".format(x)
   r = requests.get(URL, headers=headers)
   file = r.content
   table = pd.read_html(file)
   dataFrames["df{0}".format(x)] = table[1]
   print ('table',x)
   print(table[1])

print("All info gathered")

#Yhdistetään kaikkii dataFramet yhdeksi isoksi ja talletetaan excel tiedostona
result = pd.concat(dataFrames)
result.to_excel('Poromagia_Card_Database.xlsx')
print("Data saved")