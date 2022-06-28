from curses.ascii import isalpha
import json
import random
from tkinter import font
import pygame as pg
import requests

# CORES

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def	make_request(letra):
	url = 'http://papalavras-server.herokuapp.com/words/random/' + letra
	try:
		req = requests.get(url)
		dicionario = json.loads(req.text)
		return dicionario
	except Exception as e:
		print("Request mal sucedido. Erro: " + e)
		return None

def	draw_elements(window):
	gallows_img = pg.image.load('forca.png')
	font = pg.font.SysFont('Courier New', 50)
	font_rb = pg.font.SysFont('Courier New', 35, True)
	text = font_rb.render('RESTART', True, white)
	window.fill(white)
	window.blit(gallows_img, (50, 50))
	pg.draw.rect(window, black, pg.Rect(480, 60, 180, 70))
	window.blit(text, (500, 75))

def	start_window(window):
	pg.init()
	pg.font.init()
	draw_elements(window)
	pg.display.flip()

def	choose_word():
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	letter = random.choice(alphabet)
	flag = True
	dictionary = make_request(letter)
	word = dictionary["word"]
	if not word.isalpha():
		choose_word()
		

def	game(window):
	choose_word()

window = pg.display.set_mode((720, 480))
start_window(window)
game(window)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			quit()
		if event.type == pg.MOUSEBUTTONUP:
			mouse = pg.mouse.get_pos()
			if pg.Rect.collidepoint(pg.Rect(480, 60, 180, 70), mouse):
				print('clicou')
	pg.display.flip()