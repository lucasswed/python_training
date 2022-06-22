from curses.ascii import isalpha
import json
import random 
import pygame as pg
import requests

def make_request(letra):
	url = 'http://papalavras-server.herokuapp.com/words/random/' + letra
	try:
		req = requests.get(url)
		dicionario = json.loads(req.text)
		return dicionario
	except Exception as e:
		print("Request mal sucedido. Erro: " + e)
		return None


# CORES

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Abrir uma janela

pg.init()
window = pg.display.set_mode((720, 480)) # Abre uma janela
pg.display.set_caption('Jogo da Forca') # Altera o nome da janela para 'Jogo da forca'

forca_img = pg.image.load('forca.png') # Carrega a imagem
window.fill(branco)
window.blit(forca_img, (50, 50))
pg.draw.circle(window, preto, (156.5, 99), 30, 3) #cabeca
pg.draw.line(window, preto, (156.5, 129), (156.5, 189), 5) #corpo
pg.draw.line(window, preto, (156.5, 189), (186.5, 219), 5) #perna direita
pg.draw.line(window, preto, (156.5, 189), (126.5, 219), 5) #perna esquerda
pg.draw.line(window, preto, (156.5, 129), (186.5, 179), 5)
pg.draw.line(window, preto, (156.5, 129), (126.5, 179), 5)




# pg.draw.line(window, preto, False, )

while True:
	pg.display.update()


# alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# letra = random.choice(alfabeto)
# choice = True
# while choice:
# 	choice = False
# 	dicionario = make_request(letra)
# 	palavra = dicionario["word"]
# 	for c in palavra:
# 		if not isalpha(c):
# 			choice = True


# # lines =  400 / (dicionario["count"] * 2)

# lifes = 5
# correct_guesses = ''
# flag = len(palavra)
# print('lifes: ' + str(lifes))

# while lifes > 0:
# 	flag = len(palavra)

# 	for char in palavra:
# 		if char in correct_guesses:
# 			flag -= 1
# 			print(char)
# 		else:
# 			print('-')
# 	if flag == 0:
# 			print('Congrats! You win!')
# 			break

# 	guess = input('Take your guesses: ')

# 	if guess not in correct_guesses:
# 		if guess in palavra:
# 			print('Correct guess')
# 			correct_guesses += guess
# 		else:
# 			print('Wrong guess')
# 			lifes -= 1
# 			print('lifes: ' + str(lifes))
# if lifes == 0:
# 	print('You lose!')
# 	print(f"The word was {palavra}")



# Desenhar os elementos iniciais
# Se alguma letra for descoberta, substituir o traco pela letra correspondente
# Se ganhar, printar na janela que ganhou
# Se perder todas as vidas printar que perdeu

# palavras = ['rainbow', 'computer', 'science', 'programming', 
# 			'python', 'mathematics', 'player', 'condition', 
# 			'reverse', 'water', 'board', 'geeks']

# palavra = random.palavra(palavras)
# lifes = 5
# correct_guesses = ''
# print('The word has been chosen!')
# flag = len(palavra)
# print('lifes: ' + str(lifes))

# while lifes > 0:
# 	flag = len(palavra)

# 	for char in palavra:
# 		if char in correct_guesses:
# 			flag -= 1
# 			print(char)
# 		else:
# 			print('-')
# 	if flag == 0:
# 			print('Congrats! You win!')
# 			break

# 	guess = input('Take your guesses: ')

# 	if guess not in correct_guesses:
# 		if guess in palavra:
# 			print('Correct guess')
# 			correct_guesses += guess
# 		else:
# 			print('Wrong guess')
# 			lifes -= 1
# 			print('lifes: ' + str(lifes))
# if lifes == 0:
# 	print('You lose!')



