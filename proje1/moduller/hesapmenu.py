def topla():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a + b}")

def cikar():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a - b}")

def carp():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a * b}")

def bol():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    if b != 0:
        print(f"Sonuç: {a / b}")
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")

def ustal():
    a = float(input("Taban sayıyı girin: "))
    b = float(input("Üs sayıyı girin: "))
    print(f"Sonuç: {a ** b}")



def hmenu():
    while True:
        print("\033[1;32;40m")
        print("╔═════════════════════╗")
        print("║   HESAP MAKİNESİ    ║")
        print("║                     ║")
        print("║  1-Toplama          ║")
        print("║  2-Çıkarma          ║")
        print("║  3-Çarpma           ║")
        print("║  4-Bölme            ║")
        print("║  5-Üst Alma         ║")
        print("║  6-Çıkış            ║")
        print("║                     ║")
        print("║    Seçimiz nedir?   ║")
        print("╚═════════════════════╝")
        secim = input()

        if secim == "1":
            topla()
        elif secim == "2":
            cikar()
        elif secim == "3":
            carp()
        elif secim == "4":
            bol()
        elif secim == "5":
            ustal()
        elif secim == "6":
            print("Çıkış yapılıyor")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

