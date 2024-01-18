import pygame, sys, random
from pygame.math import Vector2

class cat:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('cat/graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('cat/graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('cat/graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('cat/graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('cat/graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('cat/graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('cat/graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('cat/graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('cat/graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('cat/graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('cat/graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('cat/graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('cat/graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('cat/graphics/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('cat/sound/crunch.wav')
    
    def draw_cat(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            # Direction of the head and tail

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)  
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_cat(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:    
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.cat = cat()
        self.fruit = FRUIT()

    def update(self):
        self.cat.move_cat()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_ground()
        self.fruit.draw_fruit()
        self.cat.draw_cat()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.cat.body[0]:
          self.fruit.randomize()
          self.cat.add_block()
          self.cat.play_crunch_sound()
        
        for block in self.cat.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.cat.body[0].x < cell_number or not 0 <= self.cat.body[0].y < cell_number:
            self.game_over()
        
        for block in self.cat.body[1:]:
            if block == self.cat.body[0]:
                self.game_over()

    def game_over(self):
        self.cat.reset()

    def draw_ground(self):
        ground_color = (37,37,37)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        ground_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,ground_color,ground_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        ground_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,ground_color,ground_rect)

    def draw_score(self):
        score_text = str(len(self.cat.body) - 3)
        score_surface = game_font.render(score_text,True,(129,79,22))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 10,apple_rect.height)

        pygame.draw.rect(screen,(250,250,250),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(129,79,22),bg_rect,2)

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock() # Clock to limit the frame rate
apple = pygame.image.load('cat/graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('cat/font/PoetsenOne-Regular.ttf',25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    # Draw all our elements (Background, cat, food, score, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.cat.direction.y != 1:
                    main_game.cat.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.cat.direction.x != -1:
                    main_game.cat.direction = Vector2(1,0)        
            if event.key == pygame.K_DOWN:
                if main_game.cat.direction.y != -1:
                    main_game.cat.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.cat.direction.x != 1:
                    main_game.cat.direction = Vector2(-1,0)
            

    screen.fill((72,72,72)) # Fill the screen with a gray color
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) # Limit the frame rate to 60 fps
