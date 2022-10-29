import random

list_vogals = ['a', 'e', 'i', 'o', 'u']
vogals = list()


name = input('Qual é o seu nome? ').strip().lower()

while name.isdigit() or len(name) < 3:
    name = input('Seu nome foi digitado incorretamente, favor inserir novamente: ')
    

def Newname(arg):
    for letter in arg:
        if letter in list_vogals:
            arg = arg.replace(letter, random.choice(list_vogals))
        else:
            continue
    return arg

new_name = Newname(name)

print(f'Olá senhor {new_name}! Tenha paciência comigo estou aprendendo os nomes.', end=' ')

if new_name == name:
    print(f'Olha, sei falar seu nome de primeira {new_name}')

else:
    print(f'Desculpe {new_name}. Vou tentar novamente..', end =' ')
    new_name = Newname(name)
    while new_name != name:
        print(f'{new_name}..', end = ' ')
        new_name = Newname(name)
    
    print(f'Ah agora já sei pronunciar seu nome. Mil desculpas {new_name.capitalize()}')
    

