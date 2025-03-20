from pygame import *

win_width = 1080
win_height = 480

window = display.set_mode((win_width,win_height))  #*    Создание окна 
display.set_caption('Labиринт')
FPS = 60
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 230:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 230:
            self.rect.y += self.speed
#*  <-- Объекты -->
player_l = Player('player.png', 10, 10, 40, 240, 5)
player_r = Player('player.png', 1030, 10, 40, 240, 5)
ball = GameSprite('ball.png', 540, 215, 30, 30, 5)

#? <-- Шрифты -->
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'Player 1 lose', True, (180,0,0)
)
font2 = font.Font(None, 35)
lose2 = font2.render(
    'Player 2 lose', True, (180,0,0)
)

#? <------------------>
speed_x = 5
speed_y = 5
game = True
finish = False
while game:                             #!  ИГРОВОЙ ЦИКЛ
    window.fill((0,0,0))
    player_l.update_l()
    player_l.reset()
    player_r.update_r()
    player_r.reset()
    ball.reset()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish =  True
        window.blit(lose1, (200,200))
    if ball.rect.x > 1080:
        finish =  True
        window.blit(lose2, (200,200))
    for e in event.get():
        
        if e.type == QUIT:

            game = False

    clock.tick(FPS)
    display.update()