import pandas as pd

df = pd.read_excel('tiamat_Tilaus.xlsx')
df = pd.DataFrame(df.name.str.split(' ',1).tolist(),
                                 columns = ['amount','name'])
df['amount'] = df['amount'].str.replace('x', '')
print(df)

df.to_excel('tiamat_Tilausformated.xlsx')