import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from time import sleep
import urllib.request
from PIL import Image
import emoji
import cv2
import os

pokemon = str(input('Insira o nome ou o número do pokemón: ')).strip().lower()
options_off = ['is_default','order','location_area_encounters', 'held_items','game_indices','past_types', 'name', 'species']
tab = '    '

def main():
    while True:
        try:
            api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            rest = requests.get(api)
            poke = rest.json()
            break
        except requests.exceptions.JSONDecodeError:
            print('Pokémon inválido')
    return poke

def GetOptions(poke):
    print(f"- -> Lista de opções: {' ':17}-")
    sleep(0.5)
    print(f"-{' ':38}-")
    options = []
    for name in poke:
        if name in (options_off):
            continue
        options.append(name)
    for p, i in enumerate(options):
        if i == 'id':
            i = 'number'
        if len(str(p+1)) > 1:
            print(f'-{tab}{p+1}- {i}{" "*(30-len(i))}-')
        else:
            print(f'-{tab}{p+1}- {i}{" "*(31-len(i))}-')
        print('-'*40)
        sleep(0.2)
    print(f'-{tab}{p+2}- Todas as opções{" "*(21-len(i))}-')
    print('-'*40)
    print(f'-{tab}99- Fechar Pokédex{" "*(22-len(i))}-')
    print('-'*40)

def Options(op):
    if op == 1:
        GetAbility(main())
    elif op == 2:
        GetBaseExp(main())
    elif op == 3:
        GetForms(main())
    elif op == 4:
        GetHeight(main())
    elif op == 5:
        GetNumber(main())
    elif op == 6:
        GetMoves(main())
    elif op == 7:
        GetImage(main())
    elif op == 8:
        GetStats(main())
    elif op == 9:
        GetTypes(main())
    elif op == 10:
        GetWeight(main())
    elif op == 11:
        GetAllOptions(main())
    else:
        print('Ok. Fechando Pokédex. Até mais!')
        sleep(2)
        exit

def GetAbility(poke):
    print('-> Abilities: ')
    sleep(0.3)
    for p, i in enumerate(poke['abilities']):
        print(f"{tab}- {i['ability']['name']}")
        sleep(0.1)
    ReturnMenu()
    
def GetBaseExp(poke):
    print('-> Base Experience: ', end='')
    sleep(0.3)
    base_exp = poke['base_experience']
    print(base_exp)
    ReturnMenu()

def GetForms(poke):
    print('-> Qty_forms: ', end='')
    sleep(0.3)
    qty_forms = 0
    for p, i in enumerate(poke['forms']):
        qty_forms = p
    print(qty_forms + 1)
    ReturnMenu()

def GetHeight(poke):
    print('-> Height: ', end='')
    sleep(0.3)
    height = poke['height'] / 10
    print(f'{height} cm')
    ReturnMenu()

def GetMoves(poke):
    print('-> Moves: ')
    sleep(0.3)
    for p, i in enumerate(poke['moves']):
        print(f"{tab}{p+1}-{i['move']['name']}")
        sleep(0.1)
    ReturnMenu()
        
def GetNumber(poke):
    print('-> Number: ', end='')
    sleep(0.3)
    number = poke['id']
    print(number)
    ReturnMenu()

def GetStats(poke):
    print('-> Stats:\n')
    sleep(0.3)
    for i in poke['stats']:
        sleep(0.2)
        if i ['stat']['name'] == 'hp':
            print(emoji.emojize(f"{tab}:red_heart:  {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'attack':
            print(emoji.emojize(f"{tab}:crossed_swords:  {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'defense':
            print(emoji.emojize(f"{tab}:shield:  {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'special-attack':
            print(emoji.emojize(f"{tab}:sparkles: {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'special-defense':
            print(emoji.emojize(f"{tab}:cross_mark: {i['stat']['name']}"), end=': ') 
        elif i ['stat']['name'] == 'speed':
            print(emoji.emojize(f"{tab}:running_shoe: {i['stat']['name']}"), end=': ') 
        else:
            print(emoji.emojize(f"{tab}:check_mark: {i['stat']['name']}"), end=': ')

        print(i['base_stat'])
        ReturnMenu()
        
def GetTypes(poke):
    print('-> Types: ', end='')
    sleep(0.3)
    for i in poke['types']:
        sleep(0.1)
        print(i['type']['name'])
    ReturnMenu()

def GetWeight(poke):
    print('-> Weight: ', end='')
    sleep(0.3)
    weight = poke['weight'] / 10
    print(f'{weight} kg')
    ReturnMenu()
     
def GetImage(poke):
    sprites = {
        key:value
    
        for key, value in poke['sprites'].items()  
    }
    default_image = sprites['front_default']
    urllib.request.urlretrieve(f'{default_image}', 'default_poke.png')
    image = Image.open('default_poke.png').convert('L')
    size =(200,200)
    new_image = image.resize(size)
    new_image.show()
    os.remove('default_poke.png')
    ReturnMenu()

def GetAllOptions(poke):
    GetAbility(main())
    print()
    GetBaseExp(main())
    print()
    GetForms(main())
    print()
    GetHeight(main())
    print()
    GetNumber(main())
    print()
    GetMoves(main())
    print()
    GetStats(main())
    print()
    GetTypes(main())
    print()
    GetWeight(main())
    print(f'\n-> Sprites:\n{tab}- Gerando default sprite...')
    sleep(1)
    GetImage(main())
    print('Obrigado por utilizar a Pokédex. Até mais!')


def ReturnMenu():
    while op_choiced != 11:
        print()
        sleep(1)
        menu = str(input('Deseja ver as opções novamente? [S/N] ')).strip().lower()
        if menu == 's':
            print()
            GetOptions(poke)
            new_op = int(input('Selecione o número da opção desejada: '))
            print()       
            Options(new_op)
        else:
            print('Fechando Pokédex. Até mais!')
            sleep(1)
            exit
            break
    pass
poke = main()
sleep(1)
print('Inicializando Pokédex..')
sleep(1)
print('-'*40)
print(f"-{' ':38}-")
print(emoji.emojize(f'-{"~~ Bem-vindo a Pokédex:mobile_phone:~~":^50}-'))
print(f"-{' ':38}-")
print('-'*40)
sleep(1)
GetOptions(poke)
print()
print('*Para fechar digite 99 ou qualquer outro número!')
op_choiced = int(input('Selecione o número da opção desejada: '))
print()       
Options(op_choiced)


    

if __name__ == '__main__':
    main()