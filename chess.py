import pygame as pg

pg.init()

WIDTH = 500
LENGTH = 500

display = pg.display.set_mode((WIDTH, LENGTH))
pg.display.set_caption("Chess")

def exit_game():
  pg.quit()
  exit()

def main_menu():
  menu = True
  while menu:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        exit_game()

main_menu()
pg.quit()
