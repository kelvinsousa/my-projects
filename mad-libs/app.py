

# verb1 = input(str('Verb 1: ')).strip()
# verb2 = input(str('Verb 2: ')).strip()
# famous_person = input(str('Famous Person: ')).strip()



def madlib(adj, verb1, verb2, famous_person):
    print(f'computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. \nStay hydrated and {verb2} like you are {famous_person}!')

def Check(input_list):
    
    for items in input_list:
        if items.isdigit():
            print(f'O valor {items} digitado é inválido!')
            break
    else:
        print('Valores válidos')
        madlib(adj, verb1, verb2, famous_person)





answer = []
adj = input('Adjective: ').strip()
answer.append(adj)
verb1 = input(str('Verb 1: ')).strip()
answer.append(verb1)
verb2 = input(str('Verb 2: ')).strip()
answer.append(verb2)
famous_person = input(str('Famous Person: ')).strip()
answer.append(famous_person)

        
Check(answer)

    
