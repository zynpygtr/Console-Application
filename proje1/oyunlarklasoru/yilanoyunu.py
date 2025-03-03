import pygame
import time
import random

def yilanOyna():
    

    # Pygame'i başlat
    pygame.init()

    # Oyun ekranı boyutları
    beyaz = (255, 255, 255)
    siyah = (0, 0, 0)
    kirmizi = (213, 50, 80)
    yesil = (0, 255, 0)
    mavi = (50, 153, 213)

    dis_w = 600
    dis_h = 400

    dis = pygame.display.set_mode((dis_w, dis_h))
    pygame.display.set_caption('Yılan Oyunu')

    # Saat ve yazı fontları
    clock = pygame.time.Clock()
    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    # Puan gösterimi
    def your_score(score):
        value = score_font.render("Puan: " + str(score), True, siyah)
        dis.blit(value, [0, 0])

    # Yılanın başını çizme
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, yesil, [x[0], x[1], snake_block, snake_block])

    # Mesaj yazdırma
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_w / 6, dis_h / 3])

    # Ana oyun fonksiyonu
    def gameLoop():
        game_over = False
        game_close = False

        # Yılanın başlangıç pozisyonu
        x1 = dis_w / 2
        y1 = dis_h / 2

        # Yılanın hareketi
        x1_change = 0
        y1_change = 0

        # Yılanın gövde kısmı
        snake_List = []
        Length_of_snake = 1

        # Yem pozisyonu
        foodx = round(random.randrange(0, dis_w - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_h - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                dis.fill(mavi)
                message("Kaybettin! Q-Quit veya C-Oynat tekrar", kirmizi)
                your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            # Yılanın ekran dışında çıkmaması için kontrol
            if x1 >= dis_w or x1 < 0 or y1 >= dis_h or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(mavi)
            pygame.draw.rect(dis, siyah, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            your_score(Length_of_snake - 1)

            pygame.display.update()

            # Yılan yemeği yediğinde
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_w - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_h - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    # Oyunu başlat
    gameLoop()
