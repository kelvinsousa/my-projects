import pandas as pd

df = pd.read_csv('grupos.csv')
names = []
for i in df['name'][1].str.capitalize():
    names.append(i)
print

#df.sample(n=10)['name'].to_excel('C:/Users/carla.frazzatto.AO3/PycharmProjects/ListaPython/teste2.xlsx')
