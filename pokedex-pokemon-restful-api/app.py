import requests
from time import sleep
import urllib.request
from PIL import Image
import emoji
import os

options_off = ['is_default','order','location_area_encounters', 'held_items','game_indices','past_types', 'name', 'species'] # lista das categorias que iremos decartar.

tab = '    ' # para facilitar o uso nos prints.

# funcao principal que recebe o input do Pokémon, faz o request e retorna um json com os dados do Pokémon.
    
def main():
    while True:
        try:
            pokemon = str(input('Insira o nome ou o número do pokemón: ')).strip().lower()
            api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            rest = requests.get(api)
            poke = rest.json()
            return poke
        except requests.exceptions.JSONDecodeError:
            print('Pokémon inválido')

#Funcao para pegar as opções do json, é realizado uma iteração e adicionado as opções em uma lista chamada options.
def GetOptions(poke):
    print('-'*40)
    print(f"- -> Lista de opções: {' ':17}-")
    print('-'*40)
    sleep(0.5)
    options = []
    for name in poke:
        if name in (options_off): #elimina opções que não queremos.
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

# Funcao(hub) que de acordo com a opção digitada chama outra função. 
def Options(op):
    if op == 1:
        GetAbility(poke)
    elif op == 2:
        GetBaseExp(poke)
    elif op == 3:
        GetForms(poke)
    elif op == 4:
        GetHeight(poke)
    elif op == 5:
        GetNumber(poke)
    elif op == 6:
        GetMoves(poke)
    elif op == 7:
        GetImage(poke)
    elif op == 8:
        GetStats(poke)
    elif op == 9:
        GetTypes(poke)
    elif op == 10:
        GetWeight(poke)
    elif op == 11:
        GetAllOptions(poke)
    else:
        print('Ok. Fechando Pokédex. Até mais!')
        sleep(2)
        exit()
        
def GetName(poke):
    return poke['name']

# Funcao para pegar a habilidade.
def GetAbility(poke):
    print('-> Abilities: ')
    sleep(0.3)
    for p, i in enumerate(poke['abilities']):
        print(f"{tab}- {i['ability']['name']}")
        sleep(0.1)
    ReturnMenu()

# Funcao para pegar a Exp Base   
def GetBaseExp(poke):
    print('-> Base Experience: ', end='')
    sleep(0.3)
    base_exp = poke['base_experience']
    print(base_exp)
    ReturnMenu()

# Funcao para pegar a quantidade de formas.
def GetForms(poke):
    print('-> Qty_forms: ', end='')
    sleep(0.3)
    qty_forms = 0
    for p, i in enumerate(poke['forms']):
        qty_forms = p
    print(qty_forms + 1)
    ReturnMenu()

# Funcao para pegar a altura e converter em cm.
def GetHeight(poke):
    print('-> Height: ', end='')
    sleep(0.3)
    height = poke['height'] / 10
    print(f'{height} cm')
    ReturnMenu()

# Funcao para pegar os movimentos com index.
def GetMoves(poke):
    print('-> Moves: ')
    sleep(0.3)
    for p, i in enumerate(poke['moves']):
        print(f"{tab}{p+1}-{i['move']['name']}")
        sleep(0.1)
    ReturnMenu()
        
# Funcao para pegar o número do Pokémon.
def GetNumber(poke):
    print('-> Number: ', end='')
    sleep(0.3)
    number = poke['id']
    print(number)
    ReturnMenu()

# Funcao para pegar os Stats. É inserido Emojis de acordo com os stats.
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
 
# Funcao para pegar os tipos.       
def GetTypes(poke):
    print('-> Types: ', end='')
    sleep(0.3)
    for i in poke['types']:
        sleep(0.1)
        print(i['type']['name'])
    ReturnMenu()

# Funcao para pegar o peso e converter em kg.
def GetWeight(poke):
    print('-> Weight: ', end='')
    sleep(0.3)
    weight = poke['weight'] / 10
    print(f'{weight} kg')
    ReturnMenu()
    
# Funcao para pegar o default sprite.
def GetImage(poke):
    sprites = {
        key:value
    
        for key, value in poke['sprites'].items()  
    }
    default_image = sprites['front_default']
    urllib.request.urlretrieve(f'{default_image}', 'default_poke.png')
    image = Image.open('default_poke.png').convert('L')
    size =(300,300)
    new_image = image.resize(size)
    new_image.show()
    os.remove('default_poke.png')
    ReturnMenu()

# Funcão que traz todas as opções de uma vez caso o usuário escolha.
def GetAllOptions(poke):
    GetAbility(poke)
    print()
    GetBaseExp(poke)
    print()
    GetForms(poke)
    print()
    GetHeight(poke)
    print()
    GetNumber(poke)
    print()
    GetMoves(poke)
    print()
    GetStats(poke)
    print()
    GetTypes(poke)
    print()
    GetWeight(poke)
    print(f'\n-> Sprites:\n{tab}- Gerando default sprite...')
    sleep(2)
    GetImage(poke)
    print('Obrigado por utilizar a Pokédex. Até mais!')
    exit()


# Funcao de retorno ao menu para ser aplicado nas funções, desconsiderando se o usuário escolheu para ver todas de uma vez.
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
            exit()
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
poke_choiced = GetName(poke)
print(emoji.emojize(f' Pokémon: {poke_choiced} :star:'))
sleep(1)
GetOptions(poke)
print()
print('*Para fechar digite 99 ou qualquer outro número!')
op_choiced = int(input('Selecione o número da opção desejada: '))
print()       
Options(op_choiced)


    

if __name__ == '__main__':
    main()