import random
from time import sleep

# Escolhendo uma palavra secreta do arquivo lista-palavras.txt        
def PalavraSecreta():
    with open('C:\\github\\My-Projects\\jogo-da-forca\\lista-palavras.txt', encoding='utf-8') as palavras:
        lista_palavras = []
    
        for i in palavras:
            lista_palavras.append(i.strip())
      
    return random.choice(lista_palavras)
    # print(palavras.closed)    

palavra_secreta = PalavraSecreta()

# criando a parte visual do segredo (ocultando as letras)
segredo = '_' *len(palavra_secreta)

#criando uma lista com as letras digitadas
letras_digitadas = []

#variável com o número de tentativas
tentativa = 7
print()
print(f'{"Bem-vindo ao Jogo da Forca!":.^50}')
print('\nGerando a palavra secreta...\n')
sleep(2)
print(f'Palavra com {len(palavra_secreta)} letras: ', end='')
print(f'Você tem {tentativa} tentativas! Boa sorte')
print(segredo)
print()

# função que verifica se a letra digitada está presenta na palavra secreta
def Verificacao(letra, palavra):
    adivinha = ''
    for p, l in enumerate(palavra):
        if letra == l:
            adivinha += letra # preenche a letra correta
        else:
            adivinha += segredo[p] # preenche '_' 
    return adivinha


# função que registra as tentativas e desconta uma se a letra não tiver na palavra
def Tentativas():
    global letra
    global tentativa
    if letra in palavra_secreta:
        pass
    else:
        tentativa -= 1
        print(f'\nA palavra secreta não contém a letra {letra}.')
        if tentativa != 0:
            print(f'Restam ainda {tentativa} chances.\n')
        else:
            print('Acabaram as chances :/\n')
        
# funcao que check se foi digitado apenas uma letra mesmo
def CheckChar(letra):
    if len(letra) != 1:
        print('Você digitou uma letra inválida!')
        letra = input('Digite outra letra: ').strip().upper()
    return letra    


# Enquantos as tentativas são maiores que zero o bloco abaixo vai executar
while tentativa > 0:
    
    letra = str(input('Digite uma letra: ')).strip().upper()
    letra = CheckChar(letra)
    
    if letra not in letras_digitadas:
        letras_digitadas.append(letra)
        segredo = Verificacao(letra, palavra_secreta)
        Tentativas()
        print(segredo)
        if segredo == palavra_secreta:
            print(f'Parabéns, você venceu!! A palavra secreta era {palavra_secreta}')
            break
    else:
        print('\nJá foi digitado essa letra..', end = '')
        continue
else:    
    print(f'Ihh.. não foi dessa vez, vamos revelar a palavra secreta acima {palavra_secreta}')
    sleep(1)
    print(segredo)


