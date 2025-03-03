import oyunlarklasoru


def oyunmenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOREL APP    \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Adam asmaca      ║")
    print("║  2-Tetris           ║")
    print("║  3-Yılan            ║")
    print("║  4-                 ║")
    print("║  5-Ana menü         ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" : print("Adam asmaca oyunu başlıyor..")
    if secim == "2" : print("Tetris oyunu başlıyor..")
    if secim == "3" : 
        oyunlarklasoru.yilanoyunu.yilanOyna()
    if secim == "9" : exit()
    