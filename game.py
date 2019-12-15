import pygame
from random import randint



player_x, player_y = 100,400
width, height = 400,600
FPS = 60

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 500)
pygame.display.set_caption('Rocket Game')

list_tuple = ('enemy.png','enemy2.png','enemy3.png')
list_main = []
bullet_list = []
sc = pygame.display.set_mode((width,height))

pygame.mixer.music.load('soundtrack.mp3')
bruh = pygame.mixer.Sound('bruh.wav')
blast = pygame.mixer.Sound('blast.wav')
pygame.mixer.music.play()

for i in range(len(list_tuple)):
    list_main.append(pygame.image.load(list_tuple[i]).convert_alpha())
 
player = pygame.image.load('rocket_player.png').convert_alpha()
bullet = pygame.image.load('bullet1.png').convert_alpha()
bullet_list.append(bullet)
font = pygame.font.Font(pygame.font.match_font('dejavusans'), 36)
text1 = font.render('Game over', 1, (180,0,0))


clock = pygame.time.Clock()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x,20))
        self.add(group)
        self.speed = randint(1,3)

    def update(self):

        if pygame.sprite.spritecollideany(self, bul_group) or self.rect.y > height:
            self.kill()
        else:
            self.rect.y += self.speed
    

class Player(pygame.sprite.Sprite):
    def __init__(self,x,surf):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.rotate(surf,0)
        self.rect = self.img.get_rect(center=(x,height))


class Bullet(pygame.sprite.Sprite): 
    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, height))
        self.add(group)

    def update(self):
        if self.rect.y > 0:
            self.rect.y -= 10
        else:
            self.kill()


groups = pygame.sprite.Group()
bul_group = pygame.sprite.Group()
player_rocket = Player(width // 2, player)

pygame.display.update()


while True:

    press = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.USEREVENT:
            Enemy(randint(1,width), list_main[randint(0,2)],groups)

        elif event.type == pygame.MOUSEBUTTONUP:
            Bullet(*player_rocket.rect.center, bullet_list[0], bul_group)
            blast.play()
            
    if press[pygame.K_LEFT] and player_rocket.rect[0] > 5:
        player_rocket.rect[0] -= 5
    elif press[pygame.K_RIGHT] and player_rocket.rect[0] < 350:
        player_rocket.rect[0] += 5
               
    if pygame.sprite.spritecollideany(player_rocket, groups) != None:
        sc.fill((0,0,0))
        sc.blit(text1, (width//2, height//2))
        pygame.display.update()
        pygame.mixer.music.pause()
        bruh.play()
        break

    groups.update()
    bul_group.update()
    
    sc.fill((50,25,25))
    pygame.draw.circle(sc,(255,255,255),(randint(0,width),randint(0,height)),2)

    sc.blit(player_rocket.img, player_rocket.rect)
    groups.draw(sc)
    bul_group.draw(sc)
    
    pygame.display.update()

    clock.tick(FPS)
