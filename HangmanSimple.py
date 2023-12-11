import random
from os import system, name

#Função para limpar a tela a cada execução

def limpa_tela():
    #Windows
    if name =='nt':
        _ =system('cls')
    
    #Mac ou Linux:
    else:
        _ =system('clear')

#Função jogo
def game():
    limpa_tela()

    print('\nBem vindo ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    #Lista de palavras para o jogo
    palavras =['banana', 'abacate','uva','morango','laranja']

    #Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    #List comprehension
    letras_na_palavra =['_' for letra in palavra]

    #Número de chances
    chances = 6

    #Lista para letras erradas
    letras_erradas =[]

    #Loop enquanto número de chances for maior que zero
    while chances >0:
        print(' '.join(letras_na_palavra))
        print('\nChances restantes: ',chances)
        print('Letras erradas: ', ' '.join(letras_erradas))

        #Tentativas
        tentativa = input('\nDigite uma letra: ').lower()

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_na_palavra[index] = letra
                    index +=1
                else:
                    chances -= 1
                    letras_erradas.append(tentativa)
        
        # Venceu
        if '_' not in letras_na_palavra:
            print('\n Você venceu! A palavra era: ', palavra)
            break
    
    #Perdeu
    if '_' in palavra:
        print('Você perdeu! A palavra era: ', palavra)
    
# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")
