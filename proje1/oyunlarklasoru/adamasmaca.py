import pygame
import time
import random


pygame.init() 

def asmacaOyunu():
    # Kelimeler listesi
    kelimeler = ['python', 'programlama', 'bilgisayar', 'yazilim', 'yapayzeka', 'analiz', 'geliştirme', 'oyun']

    # Adam asmaca oyunu
    def adam_asmaca():
        # Rastgele kelime seç
        kelime = random.choice(kelimeler)
        kelime_tahmin = ['_'] * len(kelime)  # Bu, tahmin edilen harfleri gösterecek
        denemeler = 6  # Adam asmaca için 6 hakkınız var
        harfler = []
        
        print("Adam Asmaca Oyunu Başlıyor!")
        print("Kelime: " + " ".join(kelime_tahmin))
        
        while denemeler > 0:
            print(f"\nKalan Deneme Hakkınız: {denemeler}")
            print("Tahmin ettiğiniz harfler: " + ", ".join(harfler))
            print("Kelime: " + " ".join(kelime_tahmin))

            # Kullanıcıdan harf alın
            tahmin = input("Bir harf tahmin edin: ").lower()

            if len(tahmin) != 1 or not tahmin.isalpha():
                print("Lütfen yalnızca bir harf girin.")
                continue

            if tahmin in harfler:
                print("Bu harfi zaten tahmin ettiniz.")
                continue
            
            harfler.append(tahmin)

            if tahmin in kelime:
                # Eğer harf kelimede varsa, doğru tahmini güncelle
                for i in range(len(kelime)):
                    if kelime[i] == tahmin:
                        kelime_tahmin[i] = tahmin
                print("Doğru tahmin!")
            else:
                # Yanlış tahmin
                denemeler -= 1
                print(f"Yanlış tahmin! '{tahmin}' kelimede yok.")
            
            # Eğer kelimeyi doğru tahmin ettiyse kazanmış olur
            if "_" not in kelime_tahmin:
                print("\nTebrikler! Kelimeyi doğru tahmin ettiniz: " + "".join(kelime_tahmin))
                break
        else:
            print(f"\nÜzgünüm, deneme haklarınız bitti. Doğru kelime: {kelime}")

    # Oyunu başlat
    adam_asmaca()
