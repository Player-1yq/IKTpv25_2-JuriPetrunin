from module1 import lisa_andmeid


palgad=[1000,1200,2500,800,750,1200]
inimesed=["A","B","C","D","E","F"]

while 1:
    print("Valige menjüst midagi: ")
    print("1. Lisage andmed: ")
    print("2. Suurim palk: ")
    print("3. Väiksem palk: ")
    print("4. Otsida palga: ")
    print("5. Piiratud palk: ")
    print("6. Keskmine palk: ")
    print("7. Sorteerida nime jargi: ")

    while True:
        try:
            vastus=int(input("Sisestage oma valig menjüst: "))
            if vastus>0 and vastus<10:
                break
        except:
            print("Viga! Palun sisesta tegevuse number!")

    if vastus==1:
        lisa_andmeid()
    if vastus==2:
       suurim_palk()
    if vastus==3:
        vaikseim_palk()
    if vastus==4:
        palga_otsing()
    if vastus==5:
        piiratud_palk()
    if vastus==6:
        keskmine_palk()
    if vastus==7:
        sorteeri_nime_jargi()
