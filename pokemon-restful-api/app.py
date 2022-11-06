import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from time import sleep
import urllib.request
from PIL import Image
import emoji

#pokemon = str(input('Insira o nome do pokemón: ')).strip().lower()
pokemon = 'pikachu'

options_off = ['is_default','order','location_area_encounters', 'held_items','game_indices','past_types', 'name', 'species']

def GetOptions(poke):
    options = []
    for name in poke:
        if name in (options_off):
            continue
        options.append(name)
    for p, i in enumerate(options):
        if i == 'id':
            i = 'number'
        print(f'{p+1}- {i}')
        #sleep(0.3)

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
    elif op == 8:
        GetStats(main())
    elif op == 9:
        GetTypes(main())
    elif op == 10:
        GetWeight(main())
    else:
        GetAllOptions(main())

def GetAbility(poke):
    print('-> Abilities: ', end='')
    for i in poke['abilities']:
        print(i['ability']['name'], end='..')
        
def GetBaseExp(poke):
    print('-> Base Experience: ', end='')
    base_exp = poke['base_experience']
    print(base_exp)

def GetForms(poke):
    print('-> Qty_forms: ', end='')
    qty_forms = 0
    for p, i in enumerate(poke['forms']):
        qty_forms = p
    print(qty_forms + 1)

def GetHeight(poke):
    print('-> Height: ', end='')
    height = poke['height'] / 10
    print(f'{height} cm')

def GetMoves(poke):
    print('-> Moves: ', end='')
    for p, i in enumerate(poke['moves']):
        print(f"{p+1}-{i['move']['name']}", end='    ')
        
def GetNumber(poke):
    print('-> Number: ', end='')
    number = poke['id']
    print(number)

def GetStats(poke):
    print('-> Stats:\n')
    sleep(0.5)
    for i in poke['stats']:
        sleep(0.2)
        if i ['stat']['name'] == 'hp':
            print(emoji.emojize(f":red_heart:  {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'attack':
            print(emoji.emojize(f":crossed_swords:  {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'defense':
            print(emoji.emojize(f":shield:  {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'special-attack':
            print(emoji.emojize(f":sparkles: {i['stat']['name']}"), end=': ')
        elif i ['stat']['name'] == 'special-defense':
            print(emoji.emojize(f":cross_mark: {i['stat']['name']}"), end=': ') 
        elif i ['stat']['name'] == 'speed':
            print(emoji.emojize(f":running_shoe: {i['stat']['name']}"), end=': ') 
        else:
            print(emoji.emojize(f":check_mark: {i['stat']['name']}"), end=': ')

        print(i['base_stat'])

def GetTypes(poke):
    print('-> Types: ', end='')
    for i in poke['types']:
        print(i['type']['name'])

def GetWeight(poke):
    print('-> Weight: ', end='')
    weight = poke['weight'] / 10
    print(f'{weight} kg')
     
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
    return new_image.show()

def GetAllOptions(poke):
    GetAbility(main())
    GetBaseExp(main())
    GetForms(main())
    GetHeight(main())
    GetNumber(main())
    GetMoves(main())
    GetStats(main())
    GetTypes(main())
    GetWeight(main())



def main():
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    rest = requests.get(api)
    poke = rest.json()
    return poke
poke = main()


print('Lista de opções: ')


GetOptions(poke)
print()
print('Ou aperte 99 para ver todas as categorias!')

op_choiced = int(input('Selecione o número da opção desejada: '))
print()

Options(op_choiced)

#Options(op_choiced)
    #GetAbility(poke)
    #GetImage(main())
    


    

if __name__ == '__main__':
    main()