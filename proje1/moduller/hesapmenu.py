def hmmenu():
    """
       Hesap makinesi menüsü ...222
    """

    # Hesap makinesi menüsü ...

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   Hesap Makinesi Menu  \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Topla            ║")
    print("║  2-Çarp             ║")
    print("║  3-Çıkar            ║")
    print("║  4-Böl              ║")
    print("║  5-üst alma         ║")
    print("║  6-Ana menu         ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    sa1 = int(input("1.Sayı nedir?"))
    sa2 = int(input("2.Sayı nedir?"))
    if secim =="1": print(toplama(sa1,sa2))
    if secim =="2": print(carpm(sa1,sa2))
    if secim =="3": print(cıkar(sa1,sa2))
    if secim =="4": print(bol(sa1,sa2))
    if secim =="5": print(ustal(sa1,sa2))
    #if secim =="6": vektorel_app.anamenu()
    else: print("yanlış seçim yaptınız")

    def toplama(a,b):
        return a+b

    def carpm(a,b):
        return a*b

    def cıkar(a,b):
        return a-b

    def bol(a,b):
        return a/b

    def ustal(x,y):
        return x**y


