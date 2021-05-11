import pygame
import time
from pygame.locals import *
import time

######CLASSES ET FONCTIONS#####

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.png").convert()
        self.block = pygame.transform.scale(self.block,(50,50))
        self.x = 100
        self.y = 100
        self.direction = 'down' # par défaut le block part vers le bas
    
    def draw(self): # affichage écran, taille et couleur
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y)) # position initiale du block
        pygame.display.flip()
    
    # fonctions de déplacement du block
    def move_down(self):
        self.direction = 'down'
    
    def move_up(self):
        self.direction = 'up'
 
    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    # fonction de changement de direction du block
    def walk(self):
        if self.direction == 'left':
            self.x -= 20
        if self.direction == 'right':
            self.x += 20
        if self.direction == 'up':
            self.y -= 20
        if self.direction == 'down':
            self.y += 20
        
        self.draw()
    

class Game:
    def __init__(self):
        pygame.init() # initialisation de Pygame
        self.surface = pygame.display.set_mode((1000, 500)) # taille de l'écran
        self.surface.fill((255,255,255)) # couleur
        self.snake = Snake(self.surface) 
        self.snake.draw() # vient de la fonction draw, dans la classe snake = on affiche le tout

    def run(self):
        running = True # le jeu est actif une fois qu'il est lancé

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False # interruption du jeu
                    if event.key == K_UP:
                        self.snake.move_up() # changements de direction up, down, left, right
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            
            self.snake.walk() # le snake avance continuellement
            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()
    
    pygame.display.flip()

    


