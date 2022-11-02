
while True:
    full_name = input('Qual é o seu nome completo? ').strip().title()
    if len(full_name) >= 5:
        break


split_name = full_name.split(' ')

dict_name = {
    pos:name
    
    for pos, name in enumerate(split_name)
        
}


def Name(*args):
    pmax = 0
    for p in dict_name.keys():
        pmax = p
        
    for p, n in dict_name.items():
        if p == 0:
            print(f'First name: {n}')
        elif p == pmax:
            print(f'Last name: {n}')
        else:
            print(f'Middle name: {n}')

Name(dict_name)