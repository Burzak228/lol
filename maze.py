#створи гру "Лабіринт"!
from typing import Any
from pygame import * 
'''Необхідні класи''' 
  
#клас-батько для спрайтів 
 
 
class GameSprite(sprite.Sprite): 
    #конструктор класу 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        #кожен спрайт повинен зберігати властивість image - зображення 
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed 
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 

    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
          self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
          self.rect.y += self.speed        
        if keys_pressed[K_LEFT] and self.rect.x > 0:
          self.rect.x -= self.speed   
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
          self.rect.x += self.speed

class Enemy(GameSprite):
    direcktion = "right"

    def update(self): 
        if self.rect.x <= 500:
           self.direcktion = "right"
        if self.rect.x >= win_width - 80:
           self.direcktion = "left"

        if self.direcktion == "left":
           self.rect.x -= self.speed
        if self.direcktion == "right":
           self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height, ):
        super().__init__()
        self.fill_color = color

        self.wigth = wall_width
        self.height = wall_height
        self.image = Surface((self.wigth, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



#Ігрова сцена: 
win_width = 700 
win_height = 500 
 
 
window = display.set_mode((win_width, win_height)) 
display.set_caption("Maze") 
background = transform.scale(image.load("background2.png"), (win_width, win_height)) 
  
#Персонажі гри: 
player = Player("hero.png", 35, 420, 10)
player2 = Enemy("cyborg.png", 500, 300, 9)
player3 = GameSprite("treasure.png", 620, 400, 10)


wool = Wall((0, 255, 205,), 500, 200, 10, 300)
wool2 = Wall((0, 255, 205,), 500, 0, 10, 100)
wool3 = Wall((0, 255, 205,), 350, 0, 10, 400)
wool4 = Wall((0, 255, 205,), 200, 100, 10, 500)
wool5 = Wall((0, 255, 205,), 0, 370, 120, 10)

game = True 
clock = time.Clock() 
FPS = 60 
 
 
#музика 
 
  
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
 
 
    window.blit(background,(0, 0))

    player.update()
    player.reset()
    player2.update()
    player2.reset()
    player3.reset()

    wool.draw_wall()
    wool2.draw_wall()
    wool3.draw_wall()
    wool4.draw_wall()
    wool5.draw_wall()




    display.update() 
    clock.tick(FPS)