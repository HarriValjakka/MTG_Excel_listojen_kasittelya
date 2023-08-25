import pandas as pd

d = {'amount': [], 'name': [], 'combined': [], 'price Porot': [], 'price MCM': [], 'nimi + mcm hinta': []}
df_filtered2 = pd.DataFrame(data=d)

df_filtered2
df1 = pd.read_excel(r'Poromagia_Card_Database.xlsx')
df1 = df1.reset_index()
df_filtered = df1[df1['Price'] > 0.5]
df_filtered = df_filtered[df_filtered['Price'] < 50]

for index, row in df_filtered.iterrows():
    head, sep, tail = row[3].partition('(')
    head, sep, tail = head.partition('FOIL')
    row[3] = head
    print(row[3])
    df_filtered2.loc[index]=[row[5],row[3],str(row[5])+"x "+row[3],row[6],"",""]

print(df_filtered2)
df_filtered2.to_excel('output_middle_price.xlsx')

    