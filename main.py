import pygame
import time
import math
from utils import scale_image, blit_rotate_center

GRASS = scale_image(pygame.image.load("images/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("images/track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("images/track-border.png"), 0.9)
FINISH = pygame.image.load("images/finish.png")
RED_CAR = scale_image(pygame.image.load("images/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("images/green-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60

class AbstractCar:
    def __init__(self, max_vel, rotatio_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.rotatio_vel = rotatio_vel
        self.angle = 0
        
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
        
    def draw(self, win):
        blit_rotate_center(win, self.img)
        
class PlayerCar(AbstractCar):
    IMG = GREEN_CAR

def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)
        
run = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]



while run:
    clock.tick(FPS)
    draw(WIN, images)
    draw(WIN, GREEN_CAR)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
pygame.quit()
