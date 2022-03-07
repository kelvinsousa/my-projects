import pandas as pd
df = pd.read_csv('grupos.csv')

df = pd.read_excel('teste.xlsx', index_col=False)
df['name'] = df['name'].str.capitalize()
print(df.sample(n=15)['name'])

df.sample(n=10)['name'].to_excel('C:/Users/carla.frazzatto.AO3/PycharmProjects/ListaPython/teste2.xlsx')



