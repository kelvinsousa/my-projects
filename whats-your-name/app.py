import random
from time import sleep

list_vogals = ['a', 'e', 'i', 'o', 'u']
vogals = list()



while True:
    name = input('Qual é o seu nome? ').strip().lower()
    if name.isdigit() or len(name) > 3:
        break
    else: 
        print('Seu nome foi digitado incorretamente..', end=' ')
    

def Newname(arg):
    for letter in arg:
        if letter in list_vogals:
            arg = arg.replace(letter, random.choice(list_vogals))
        else:
            continue
    return arg

new_name = Newname(name)

print(f'Olá Sr(a). {new_name}! Tenha paciência comigo estou aprendendo os nomes.', end=' ')
sleep(1)
print()

if new_name == name:
    print(f'Olha, sei falar seu nome de primeira {new_name}')

else:
    print(f'Desculpe {new_name}. Vou tentar novamente..')
    sleep(0.5)
    new_name = Newname(name)
    while new_name != name:
        print(f'{new_name}..')
        sleep(0.5)
        new_name = Newname(name)
    
    print(f'Ah agora já sei pronunciar seu nome. Mil desculpas {new_name.capitalize()}.')
    

