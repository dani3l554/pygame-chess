"""
Python implementation of chess using the pygame GUI library.
By Daniel Nicholson
"""

import pygame as pg
import os
import sys

#Turns off silly deprecation warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

pg.init()

WIDTH = 400
LENGTH = 400

BUTTON_FONT = 'AppleGaramond.ttf'

BLACK = (0,0,0)
WHITE = (255,255,255)

menu_background = pg.image.load("menu_background.png")
board_img = pg.image.load("board.png")

pieces_img = {}
for file in os.listdir(r"pieces/"):
	pieces_img[file.split(".")[0]] = pg.image.load("pieces/" + file)

clock = pg.time.Clock()

display = pg.display.set_mode((WIDTH, LENGTH))
pg.display.set_caption("Chess")

menu = False

class Text:
	def __init__(self, x, y, text, font, font_size, colour):
		self.x = x
		self.y = y
		self.text = text
		self.font = font
		self.font_size = font_size
		self.colour = colour

	def gen_text_objs(self):
		font_obj = pg.font.Font(self.font, self.font_size)
		text_surface = font_obj.render(self.text, True, self.colour)
		return text_surface, text_surface.get_rect()

	def draw_text(self):
		text_surface, text_rect = self.gen_text_objs()
		text_rect.center = (self.x,self.y)
		display.blit(text_surface,text_rect)

class Button:
	def __init__(self, x, y, w, h, text, action=None):
		self.x = x - (w/2)
		self.y = y - (h/2)
		self.centre = (x, y)
		self.w = w
		self.h = h
		self.text = text
		self.action = action
		self.button_rect = (self.x,self.y,w,h)

	def draw_button(self):
		if self.is_active():
			if pg.mouse.get_pressed()[0] == 1 and self.action != None:
				self.action()
			pg.draw.rect(display, BLACK, self.button_rect)
			button_text = Text(self.centre[0],self.centre[1],self.text,BUTTON_FONT,25,WHITE)
		else:
			pg.draw.rect(display, WHITE, self.button_rect, 2)
			button_text = Text(self.centre[0],self.centre[1],self.text,BUTTON_FONT,25,BLACK)
		
		button_text.draw_text()

	def is_active(self):
		mouse = pg.mouse.get_pos()
		if mouse[0] >= self.x and mouse[0] <= self.x + self.w:
			if mouse[1] >= self.y and mouse[1] <= self.y + self.h:
				return True
		return False

class Board:
	def __init__(self):
		self.board = [["" for i in range(8)] for j in range(8)]
		self.board[0] = ["br","bn","bb","bq","bk","bb","bn","br"]
		self.board[1] = ["bp"] * 8
		self.board[6] = ["wp"] * 8
		self.board[7] = ["wr","wn","wb","wq","wk","wb","wn","wr"]
		self.w = 400
		self.h = 400
	
	def print_board(self):
		for row in self.board:
			print(row)

	def blit_board(self):
		display.blit(board_img,(0,0))

	def blit_pieces(self):
		for row_number in range(len(self.board)):
			for column_number in range(len(self.board[row_number])):
				Piece(self.board[row_number][column_number],[column_number,row_number]).blit_piece()

	def move_piece(self,prev_pos,next_pos):
		board.board[next_pos[0]][next_pos[1]] = board.board[prev_pos[0]][prev_pos[1]]
		board.board[prev_pos[0]][prev_pos[1]] = ""

class Piece:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.x = self.pos[0] * (board.w / 8) + 2.5
		self.y = self.pos[1] * (board.h / 8) + 2.5

	def blit_piece(self):
		if self.name != '':
			display.blit(pieces_img[self.name],(self.x,self.y))

def exit_game():
	pg.quit()
	exit()

def start_game():
	global menu
	menu = False

def game_loop():
	global board
	in_game = True
	board = Board()
	while in_game:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit_game()
		
		board.blit_board()
		board.blit_pieces()
		pg.display.update()
		clock.tick(20)

def main_menu():
	global menu
	menu = True
	while menu:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit_game()

		display.blit(menu_background, (0,0))
		start_button = Button(200,200,80,30,"Start",start_game)
		exit_button = Button(200,300,80,30,"Exit",exit_game)
		start_button.draw_button()
		exit_button.draw_button()

		pg.display.update()
		clock.tick(20)
	game_loop()

main_menu()
pg.quit()
