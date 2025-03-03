import random
import pygame # type: ignore
import time


def oyunmenu():
    while True:
        
        print("╔═════════════════════╗")
        print("║       OYUNLAR       ║")
        print("║                     ║")
        print("║  1-Yılan Oyunu      ║")
        print("║  2-Adam Asmaca      ║")
        print("║  3-Çıkış            ║")
        print("║                     ║")
        print("║    Seçimiz nedir?   ║")
        print("╚═════════════════════╝")
        secim = input()

        if secim == "1":
            yilanOyna()
        elif secim == "2":
            adamas()
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


def yilanOyna():

    # Ekran boyutları
    WIDTH, HEIGHT = 600, 400

    # Renkler
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (213, 50, 80)
    BLUE = (50, 153, 213)
    BLACK = (0, 0, 0)

    # Yılan ve hız ayarları
    SNAKE_BLOCK = 10
    SNAKE_SPEED = 15

    pygame.init()

    # Oyun ekranı oluşturma
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Yılan Oyunu")

    clock = pygame.time.Clock()

    # Font ayarları
    font = pygame.font.SysFont("bahnschrift", 25)

    def draw_snake(snake_block, snake_list):
        for block in snake_list:
            pygame.draw.rect(display, GREEN, [block[0], block[1], snake_block, snake_block])

    def show_message(msg, color, x, y):
        message = font.render(msg, True, color)
        display.blit(message, [x, y])

    def game_loop():
        game_over = False
        game_close = False
        
        x, y = WIDTH / 2, HEIGHT / 2
        dx, dy = 0, 0
        
        snake_list = []
        snake_length = 1
        
        food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
        food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
        
        while not game_over:
            while game_close:
                display.fill(BLUE)
                show_message("Kaybettin! Yeniden oynamak için Q'ya, çıkmak için C'ye bas", RED, 50, HEIGHT / 2)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_loop()
                        if event.key == pygame.K_c:
                            game_over = True
                            game_close = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx, dy = -SNAKE_BLOCK, 0
                    elif event.key == pygame.K_RIGHT:
                        dx, dy = SNAKE_BLOCK, 0
                    elif event.key == pygame.K_UP:
                        dx, dy = 0, -SNAKE_BLOCK
                    elif event.key == pygame.K_DOWN:
                        dx, dy = 0, SNAKE_BLOCK
            
            if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
                game_close = True
            
            x += dx
            y += dy
            
            display.fill(BLACK)
            pygame.draw.rect(display, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
            
            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)
            
            if len(snake_list) > snake_length:
                del snake_list[0]
            
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True
            
            draw_snake(SNAKE_BLOCK, snake_list)
            pygame.display.update()
            
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
                food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
                snake_length += 1
            
            clock.tick(SNAKE_SPEED)
        
        pygame.quit()
        quit()

    game_loop()


def adamas():
    # Ekran boyutları
    WIDTH, HEIGHT = 600, 400

    # Renkler
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (213, 50, 80)
    BLUE = (50, 153, 213)
    BLACK = (0, 0, 0)

    # Yılan ve hız ayarları
    SNAKE_BLOCK = 10
    SNAKE_SPEED = 15

    pygame.init()

    # Oyun ekranı oluşturma
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Yılan Oyunu")

    clock = pygame.time.Clock()

    # Font ayarları
    font = pygame.font.SysFont("bahnschrift", 25)

    def draw_snake(snake_block, snake_list):
        for block in snake_list:
            pygame.draw.rect(display, GREEN, [block[0], block[1], snake_block, snake_block])

    def show_message(msg, color, x, y):
        message = font.render(msg, True, color)
        display.blit(message, [x, y])

    def game_loop():
        game_over = False
        game_close = False
        
        x, y = WIDTH / 2, HEIGHT / 2
        dx, dy = 0, 0
        
        snake_list = []
        snake_length = 1
        
        food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
        food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
        
        while not game_over:
            while game_close:
                display.fill(BLUE)
                show_message("Kaybettin! Yeniden oynamak için Q'ya, çıkmak için C'ye bas", RED, 50, HEIGHT / 2)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_loop()
                        if event.key == pygame.K_c:
                            game_over = True
                            game_close = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx, dy = -SNAKE_BLOCK, 0
                    elif event.key == pygame.K_RIGHT:
                        dx, dy = SNAKE_BLOCK, 0
                    elif event.key == pygame.K_UP:
                        dx, dy = 0, -SNAKE_BLOCK
                    elif event.key == pygame.K_DOWN:
                        dx, dy = 0, SNAKE_BLOCK
            
            if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
                game_close = True
            
            x += dx
            y += dy
            
            display.fill(BLACK)
            pygame.draw.rect(display, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
            
            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)
            
            if len(snake_list) > snake_length:
                del snake_list[0]
            
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True
            
            draw_snake(SNAKE_BLOCK, snake_list)
            pygame.display.update()
            
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
                food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
                snake_length += 1
            
            clock.tick(SNAKE_SPEED)
        
        pygame.quit()
        quit()

    game_loop()
