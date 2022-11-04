import random
from time import sleep

        
def PalavraSecreta():
    with open('C:\\github\\My-Projects\\jogo-da-forca\\lista-palavras.txt', encoding='utf-8') as palavras:
        lista_palavras = []
    
        for i in palavras:
            lista_palavras.append(i.strip())
      
    return random.choice(lista_palavras)
    # print(palavras.closed)    

palavra_secreta = PalavraSecreta()

global tentativas


# palavra_secreta_new = {
#     posicao:letra
    
#     for posicao, letra in enumerate(palavra_secreta)
# }

segredo = '_' *len(palavra_secreta)
letras_digitadas = []
tentativa = 5

print(f'{"Bem-vindo ao Jogo da Forca!":.^50}')
print('\nGerando a palavra secreta...\n')
sleep(2)
print(f'Palavra com {len(palavra_secreta)} letras: ', end='')
print(f'Você tem {tentativa} tentativas! Boa sorte')
print(segredo)
print()

print(palavra_secreta)


def Verificacao(letra, palavra):
    adivinha = ''
    for p, l in enumerate(palavra):
        if letra == l:
            adivinha += letra
        else:
            adivinha += segredo[p]
    return adivinha


def Contador():
    global letra
    global tentativa
    if letra in palavra_secreta:
        pass
    else:
        tentativa -= 1
        print(f'\nA palavra secreta não contém a letra {letra}.')
        print(f'Restam ainda {tentativa} chances.\n')
        
def CheckChar(letra):
    if len(letra) != 1:
        print('Você digitou uma letra inválida!')
        letra = input('Digite outra letra: ').strip().upper()
    return letra    



while tentativa > 0:
    
    letra = str(input('Digite uma letra: ')).strip().upper()
    letra = CheckChar(letra)
    
    if letra not in letras_digitadas:
        letras_digitadas.append(letra)
        segredo = Verificacao(letra, palavra_secreta)
        Contador()
        print(segredo)
        if segredo == palavra_secreta:
            print(f'Parabéns, você venceu!! A palavra secreta era {palavra_secreta}')
            break
    else:
        print('\nJá foi digitado essa letra..', end = '')
        continue
else:    
    print(f'Ihh.. não foi dessa vez, a palavra secreta era {palavra_secreta}')    


