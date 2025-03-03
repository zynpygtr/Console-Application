import pygame
import time
import random

pygame.init() 

def yilanOyna():
   # Pygame'i başlat
    

    # Renkler
    beyaz = (255, 255, 255)
    siyah = (0, 0, 0)
    kirmizi = (213, 50, 80)
    yesil = (0, 255, 0)
    mavi = (50, 153, 213)

    # Ekran boyutları
    genislik = 600
    yukseklik = 400

    # Ekranı oluştur
    dislay = pygame.display.set_mode((genislik, yukseklik))
    pygame.display.set_caption('Yılan Oyunu')

    # FPS kontrolü
    clock = pygame.time.Clock()
    yilan_hiz = 15

    # Yılan özellikleri
    yilan_boyutu = 10
    yilan_hizi = 15

    # Yazı fontu
    font_style = pygame.font.SysFont("bahnschrift", 25)
    puan_fontu = pygame.font.SysFont("comicsansms", 35)

    # Puanı ekrana yazdıran fonksiyon
    def puan(puan):
        value = puan_fontu.render("Puan: " + str(puan), True, siyah)
        dislay.blit(value, [0, 0])

    # Yılanın kendisini çizdiği fonksiyon
    def yilan(yilan_boyutu, yilan_listesi):
        for x in yilan_listesi:
            pygame.draw.rect(dislay, yesil, [x[0], x[1], yilan_boyutu, yilan_boyutu])

    # Ana oyun döngüsü
    def oyun():
        oyun_bitti = False
        oyun_kapanma = False

        # Yılan başlangıç pozisyonu
        x1 = genislik / 2
        y1 = yukseklik / 2

        # Yılanın hareket ettiği hız
        x1_hareket = 0
        y1_hareket = 0

        # Yılanın vücut parçaları
        yilan_listesi = []
        uzunluk = 1

        # Yiyeceğin başlangıç pozisyonu
        yemek_x = round(random.randrange(0, genislik - yilan_boyutu) / 10.0) * 10.0
        yemek_y = round(random.randrange(0, yukseklik - yilan_boyutu) / 10.0) * 10.0

        while not oyun_bitti:

            while oyun_kapanma:
                dislay.fill(mavi)
                mesaj = font_style.render("Oyun bitti! C-Devam, Q-Çıkış", True, kirmizi)
                dislay.blit(mesaj, [genislik / 6, yukseklik / 3])
                puan(uzunluk - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            oyun_bitti = True
                            oyun_kapanma = False
                        if event.key == pygame.K_c:
                            oyun()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oyun_bitti = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_hareket = -yilan_boyutu
                        y1_hareket = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_hareket = yilan_boyutu
                        y1_hareket = 0
                    elif event.key == pygame.K_UP:
                        y1_hareket = -yilan_boyutu
                        x1_hareket = 0
                    elif event.key == pygame.K_DOWN:
                        y1_hareket = yilan_boyutu
                        x1_hareket = 0

            # Yılan ekran dışına çıkarsa oyun bitsin
            if x1 >= genislik or x1 < 0 or y1 >= yukseklik or y1 < 0:
                oyun_kapanma = True
            
            x1 += x1_hareket
            y1 += y1_hareket
            dislay.fill(mavi)
            pygame.draw.rect(dislay, siyah, [yemek_x, yemek_y, yilan_boyutu, yilan_boyutu])
            yilan_basi = []
            yilan_basi.append(x1)
            yilan_basi.append(y1)
            yilan_listesi.append(yilan_basi)
            if len(yilan_listesi) > uzunluk:
                del yilan_listesi[0]

            for x in yilan_listesi[:-1]:
                if x == yilan_basi:
                    oyun_kapanma = True

            yilan(yilan_boyutu, yilan_listesi)
            puan(uzunluk - 1)

            pygame.display.update()

            # Yılan yiyeceği yediğinde yeni yiyecek oluştur
            if x1 == yemek_x and y1 == yemek_y:
                yemek_x = round(random.randrange(0, genislik - yilan_boyutu) / 10.0) * 10.0
                yemek_y = round(random.randrange(0, yukseklik - yilan_boyutu) / 10.0) * 10.0
                uzunluk += 1

            clock.tick(yilan_hiz)

        pygame.quit()
        quit()

    # Oyunu başlat
    oyun()
