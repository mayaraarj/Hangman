# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name


#Função para limpar a tela a cada excução do programa
def limpa_tela():

     #Windows
     if name == 'nt':
          _ = system('cls')
     #Mac ou Linux
     else:
          _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra_secreta):
         self.palavra_secreta = palavra_secreta
         self.letras_corretas = []
         self.letras_erradas = []

	# Método para adivinhar a letra
     def tentativa(self,letra):
          if letra in self.palavra_secreta:
               self.letras_corretas.add(letra)
          else:
               self.letras_erradas.add(letra)

	# Método para verificar se o jogo terminou
     def jogoTerminado(self):
          return self.verificarVitoria() or self.verificarDerrota()
	
     # Método para verificar se o jogador venceu
     def verificarVitoria(self):
          for letra in self.palavra_secreta:
               if letra not in self.palavra_secreta:
                    return False
               else:
                    return True
	
     # Método para verificar derrota
     def verificarDerrota(self):
          return len(self.letras_erradas >= 6)

	# Método para não mostrar a letra no board
     def naoMostrarLetra(self,letra):
               return letra not in self.letras_corretas
     	
	# Método para checar o status do game e imprimir o board na tela
     
     def ChecaStatusImprimeBoard(self):
          palavra_mostrada = ''
     
          for letra in self.palavra_secreta:
               if letra in self.letras_corretas:
                    palavra_mostrada += letra
               else:
                    palavra_mostrada += '_'
     
          print( 'Palavra: ', palavra_mostrada)
          print("Letras corretas: ", ", ".join(self.letras_corretas))
          print("Letras erradas: ", ", ".join(self.letras_erradas))

#Jogo em ação
def main():
     limpa_tela()
     palavra_secreta = 'Agua'
     jogo = Hangman(palavra_secreta)

     while not Hangman.jogoTerminado(jogo):
          jogo.ChecaStatusImprimeBoard()
          letra = input('Digite uma letra: ')
          Hangman.tentativa(letra)

     if jogo.verificarVitoria():
          print('Parabéns! Você venceu!')
     else:
          print('Não foi dessa vez! A palavra era: ',jogo.palavra_secreta)

# Executando o programa
if __name__ == '__main__':
     main()
