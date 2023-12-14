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
          if letra in self.palavra_secreta and letra not in self.letras_corretas:
               self.letras_corretas.append(letra)
          elif letra not in self.palavra_secreta and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          return True

	# Método para verificar se o jogo terminou
     def jogoTerminado(self):
          return self.verificarVitoria() or (len(self.letras_erradas) == 6)

     # Método para verificar se o jogador venceu
     def verificarVitoria(self):
         
         if '_' not in self.naoMostrarLetra():
              return True
         else:
              return False

	# Método para não mostrar a letra no board
     def naoMostrarLetra(self):
          rtn = ''
         
          for letra in self.palavra_secreta:
               if letra not in self.letras_corretas:
                    rtn += ' _ '
               else:
                   rtn += letra
          return rtn


	# Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
          print(board[len(self.letras_erradas)])
          print('\nPalavra: '+ self.naoMostrarLetra())
          print('\nLetras erradas: ',)

          for letra in self.letras_erradas:
               print(letra,)
          
          print()

          print('Letras corretas: ',)

          for letra in self.letras_corretas:
               print(letra,)

          print()

#Método para ler uma palavra aleatória de uma lista pré-determinada
def rand_palavra():
     palavras= ['lua','chuva','terra','sol','mar']

     #Escolhe a palavra secreta randomicamente
     palavra = random.choice(palavras)
     return palavra

# Método Main - Execução do Programa
def main():

	limpa_tela()

	# Cria o objeto e seleciona uma palavra randomicamente
	jogo = Hangman(rand_palavra())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not jogo.jogoTerminado():
		
		#  Status do game
		jogo.print_game_status()
		
		# Recebe input do terminal
		usuario = input('\nDigite uma letra: ')
		
		# Verifica se a letra digitada faz parte da palavra
		jogo.tentativa(usuario)

	# Verifica o status do jogo
	jogo.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if jogo.verificarVitoria():
		print ('\nParabéns! Você venceu!!')
	
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + jogo.palavra_secreta)

# Executa o programa		
if __name__ == "__main__":
	main()