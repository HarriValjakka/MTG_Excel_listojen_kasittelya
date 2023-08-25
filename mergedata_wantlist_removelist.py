import pandas as pd
import numpy as np

df1 = pd.read_excel(r'CurrentWantAfterKonsta.xlsx')
df1 = df1.reset_index()
df2 = pd.read_excel(r'tiamat_Tilausformated.xlsx')
df2 = df2.reset_index()


for index, row in df1.iterrows():
    head, sep, tail = row[2].partition('(')
    row[2] = head
    df1.loc[row[1]]=[row[0],row[1],row[2]]


for index, row in df2.iterrows():
    head, sep, tail = row[2].partition('(')
    row[2] = head
    df2.loc[row[0]]=[row[0],row[1],row[2]]
    
for index, row in df2.iterrows():
    df1Row = df1[df1["name"] == row["name"]]
    if df1Row['amount'].values.size>0:
        val = df1Row['amount'].values[0]
        val = val - row.iloc[1]
        df1.loc[df1Row['index'].values[0]] = [df1Row['index'].values[0],val,df1Row['name'].values[0]]
    else:
        print("bad")
        print(row["name"])

df_filtered = df1[df1['amount'] > 0]
print(df_filtered)
df_filtered.to_excel('output.xlsx')