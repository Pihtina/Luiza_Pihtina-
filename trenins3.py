import pygame
import json

pygame.init()
with open('my game/levels/level1.json','r') as file:
    world_data = json.load(file)

width, height = 800, 600
clock = pygame.time.Clock()
fps = 60
tile_size = 40
game_over = 0
score = 0

sound_jump = pygame.mixer.Sound('my game/images/jump.wav')
sound_game_over = pygame.mixer.Sound('my game/images/game_over.wav')


door_image = pygame.image.load('my game/images/door1.png') 
coin_image = pygame.image.load('my game/images/diamond2.png')

with open('my game/levels/level1.json', 'r') as file:
    world_data = json.load(file)
level = 1
max_level = 3

def reset_level():
    player.rect.x = 100
    player.rect.y = height - 130
    lava_group.empty()
    exit_group.empty()
    with open(f'my game/levels/level{level}.json', 'r') as file:
        world_data = json.load(file)
    world = World(world_data)
    return world

class World:
    def __init__(self,data):
        dirt_image = pygame.image.load('my game/images/dirt.png')
        grass_image = pygame.image.load('my game/images/grass (2).png')
        self.title_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 2:
                    images = {1:dirt_image, 2:grass_image }
                    img = pygame.transform.scale(images[tile],
                                                 (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.title_list.append(tile)
                elif tile == 3:
                    lava = Lava(col_count * tile_size,
                                row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                elif tile == 5:
                    exit = Exit(col_count * tile_size,
                                row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                elif tile == 6:
                    coin = Coin(col_count * tile_size + (tile_size // 2),
                                                         row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                    
                col_count += 1
            row_count += 1
    def draw (self):
        for tile in self.title_list:
            display.blit(tile[0], tile[1])


display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer")
bg_image = pygame.image.load('my game/images/bg11.png')
grass_image = pygame.image.load('my game/images/grass.png')
start_image = pygame.image.load('my game/images/start_btn 4.png')

lives = 3

def draw_text(text, color, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    img = font.render(text, True, color)
    display.blit(img,(x, y))


class Player:
    def __init__(self):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.direction = 1  

        
        for num in range(1, 5):
            img = pygame.image.load(f'my game/images/player{num}.png')
            img = pygame.transform.scale(img, (35, 70))
            self.images_right.append(img)
            self.images_left.append(pygame.transform.flip(img, True, False)) 

        self.image = self.images_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = height - 130

        self.gravity = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.jumped = False

    def update(self):
        global game_over
        
        walk_speed = 5
       
        if game_over == 0: 
            x = 0
            y = 0
           
            

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.gravity = -15
                self.jumped = True
                sound_jump.play()
            if key[pygame.K_LEFT]:
                x -= 1
            if key[pygame.K_RIGHT]:
                x += 1
                    
            if key[pygame.K_LEFT]:
                x -= walk_speed
                self.direction = -1
                self.counter += 1
            if key[pygame.K_RIGHT]:
                x += walk_speed
                self.direction = 1
                self.counter += 1
            self.gravity += 1
            if self.gravity > 10:
                self.gravity = 10
            y += self.gravity
           
            for tile in world.title_list:
                if tile[1].colliderect(self.rect.x + x, self.rect.y,
                                    self.width, self.height):
                    x = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + y,
                                    self.width, self.height):
                    if self.gravity < 0:
                        y = tile[1].bottom - self.rect.top
                        self.gravity = 0
                    elif self.gravity >= 0:
                        y = tile[1].top - self.rect.bottom
                        self.gravity = 0
                        self.jumped = False
            self.rect.x += x
            self.rect.y += y
            
        
            if self.counter > 10:
                self.counter = 0
                self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0    
            self.image = self.images_right[self.index] if self.direction == 1 else self.images_left[self.index]
            if self.rect.bottom > height:
                self.rect.bottom = height 
            
            if pygame.sprite.spritecollide(self,lava_group,False):
                game_over = -1
            
            if pygame.sprite.spritecollide(self, exit_group,False):
                game_over = 1
        elif game_over ==-1:
            print('Game over')
        
        display.blit(self.image, self.rect)
       
class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('my game/images/door1.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

exit_group = pygame.sprite.Group()


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('my game/images/coin.png')
        self.image = pygame.transform.scale(img,(tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

coin_group = pygame.sprite.Group()




class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        img = pygame.image.load(r'my game\images\tile6.png')
        self.image = pygame.transform.scale(img,
                                            (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
lava_group = pygame.sprite.Group()
class Button:
    def __init__(self,x,y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(x,y))
    def draw(self):
        action = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        display.blit(self.image,self.rect)
        return action
            
restart_button = Button(width // 2, height // 2, 'my game/images/restart_btn 2.png' )
start_button = Button(width // 2 - 150, height // 2, 'my game/images/start_btn 2.png')
exit_button = Button(width // 2 + 150, height // 2, 'my game/images/exit_btn 2.png')

world =World (world_data)
player = Player()


run = True
main_menu = True
while run:
    clock.tick(fps)
    display.blit(bg_image, (0, 0))
    if main_menu:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
            level = 1
            score = 0
            world = reset_level()   
    else:
        world.draw()
        lava_group.draw(display)
        exit_group.draw(display)
        coin_group.draw(display)
        draw_text(str(score),(255, 255, 255), 30, 10, 10)
        player.update()
        lava_group.update()

        if pygame.sprite.spritecollide(player, coin_group,True):
            score += 1
            print(score)
        if game_over == -1:
            if restart_button.draw():
                player =Player()
                # world = World(world_data)
                world = reset_level()
                game_over = 0

        if game_over == 1:
            game_over = 0
            if level < max_level:
                level += 1
                world = reset_level()
            else:
                print('win')
                main_menu = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

