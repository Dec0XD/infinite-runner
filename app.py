import pygame

WIDTH = 1200
HEIGHT = 600
SPEED = 10
Game_speed = 10
groud_width = 2 * WIDTH
groud_heigth = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [
            pygame.image.load('sprites/Run__000.png').convert_alpha(),
            pygame.image.load('sprites/Run__001.png').convert_alpha(),
            pygame.image.load('sprites/Run__002.png').convert_alpha(),
            pygame.image.load('sprites/Run__003.png').convert_alpha(),
            pygame.image.load('sprites/Run__004.png').convert_alpha(),
            pygame.image.load('sprites/Run__005.png').convert_alpha(),
            pygame.image.load('sprites/Run__006.png').convert_alpha(),
            pygame.image.load('sprites/Run__007.png').convert_alpha(),
            pygame.image.load('sprites/Run__008.png').convert_alpha(),
            pygame.image.load('sprites/Run__009.png').convert_alpha(),
        ]
        self.image_fall = pygame.image.load('sprites/Fall.png').convert_alpha()
        self.image = pygame.image.load('sprites/Run__000.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0
        
    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += Game_speed
            if key[pygame.K_a]:
                self.rect[0] -= Game_speed
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])
        
        move_player(self)
        self.rect[1] += SPEED
        
        def fly (self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= 30
                self.image = pygame.image.load('sprites/Fly.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100, 100])
                print('fly')
        fly(self)
        
        def fall(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groudGroup, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_fall
                self.image = pygame.transform.scale(self.image, [100, 100])
        fall(self)
        
class Groud(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (groud_width, groud_heigth))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - groud_heigth
    def update(self, *args):
        self.rect[0] -= Game_speed
        
def is_off_screen(sprite):
        return sprite.rect[0] < -(sprite.rect[2])



pygame.init()
game_window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Speed Runner")

BACKGROUD = pygame.image.load('sprites/background_03.jpg')
BACKGROUD = pygame.transform.scale(BACKGROUD,[WIDTH, HEIGHT])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groudGroup = pygame.sprite.Group()
for i in range(2):
    groud = Groud(WIDTH * i)
    groudGroup.add(groud)



gameloop = True
def draw():
    playerGroup.draw(game_window)
    groudGroup.draw(game_window)
    
def update():
    groudGroup.update()
    playerGroup.update()
    
clock = pygame.time.Clock()
    
while gameloop:
    clock.tick(30)
    game_window.blit(BACKGROUD, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    if is_off_screen(groudGroup.sprites()[0]):
        groudGroup.remove(groudGroup.sprites()[0])
        newGround = Groud(WIDTH - 20)
        groudGroup.add(newGround)
        
    if pygame.sprite.groupcollide(playerGroup, groudGroup, False, False):
        SPEED = 0
        print('Colision')
    else:
        SPEED = 10
        
    update()
    draw()
    pygame.display.update()