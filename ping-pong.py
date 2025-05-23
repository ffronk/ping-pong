from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


#игровая сцена:
back = transform.scale(image.load("qwerty.jpg"), (700,700)) #цвет фона (background)
win_width = 700
win_height = 680
window = display.set_mode((win_width, win_height))



#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

#шедевромузыка
mixer.init()
mixer.music.load("kruto.mp3")
mixer.music.play()

#создания мяча и ракетки   
racket1 = Player('palka.png', 30, 200, 6, 50, 150) 
racket2 = Player('palka.png', 620, 200, 6, 50, 150)
ball = GameSprite('stone.png', 200, 200, 4, 50, 50)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 CHMO!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 CHMO!', True, (180, 0, 0))


speed_x = 5
speed_y = 5


while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(back,(0, 0))
       racket1.update_l()
       racket2.update_r()
       ball.rect.x += speed_x
       ball.rect.y += speed_y


       if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
           speed_x *= -1
           speed_y *= 1
      
       #если мяч достигает границ экрана, меняем направление его движения
       if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1


       #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True


       #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
       if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True


       racket1.reset()
       racket2.reset()
       ball.reset()


   display.update()
   clock.tick(FPS)
