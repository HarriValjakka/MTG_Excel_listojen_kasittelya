import pandas as pd
import numpy as np

d = {'index': [], 'amount': [], 'name': [], 'combined': [], 'price Porot': [], 'price MCM': [], 'nimi + mcm hinta': []}
df_filtered2 = pd.DataFrame(data=d)

Missingprice=0
df1 = pd.read_excel(r'output_middle_price.xlsx')

for index, row in df1.iterrows():
    if(row[5]=="----"):
        print("missing price")
        Missingprice = Missingprice+1
        #df_filtered2.loc[index]=[row[0],row[1],row[2],row[3],row[4],row[5]]
    elif(row[5]!=""):
        row[5]=float(row[5])
        if((row[4]-row[5])>(row[4]/5)):
            df_filtered2.loc[index]=[row[0],row[1],row[2],row[3],row[4],row[5],row[6]]
    else:
        print("no value")

print(df_filtered2)
print("prices missiing")
print(Missingprice)
df_filtered2.to_excel('WorthIt.xlsx')
    