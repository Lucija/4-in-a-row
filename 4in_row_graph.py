from tkinter import *

solved = False
dim1 = int(input("Širina površine (max 26): "))
dim2 = int(input("Višina površine (max 12): "))
igralec = 1
land = {}




def slika(slovar, dim1, dim2):
    window = Tk()
    canvas = Canvas(window, width = dim1 * 50, height = dim2 * 50)
    canvas.pack()
    canvas.create_rectangle(0, 0, dim1 * 50, dim2 * 50, fill = "black")
    for k in slovar:
        if slovar[k] == 1:
            barva = "white"
        if slovar[k] == 2:
            barva = "blue"
        canvas.create_oval(k//10*50 - 50, dim2 * 50 - k%10*50, k//10*50+50 - 50, dim2 * 50 - k%10*50+50, fill = barva)
    window.mainloop()

slika(land, dim1, dim2)


while solved == False:
    if len(land) == dim1 * dim2:
        print("Ni več možnih potez.")
        solved == True
        continue
    if igralec == 1:
        x = int(input("Poteza 1. igralca: "))
    if igralec == 2:
        x = int(input("Poteza 2. igralca: "))
    if x > dim1:
        print("Napaka. Tega stolpca ni.")
        continue
##    if x > dim2:
##        print("Napaka. Ta stolpec je že zapolnjen.")
##        continue

    a = 1
    while land.get(x * 10 + a) != None:
        a += 1
    if a > dim2:
        print("Napaka. Ta stolpec je že zapolnjen.")
        continue
              
    pozicija = x * 10 + a
    land[pozicija] = igralec



    slika(land, dim1, dim2)

    
##POPRAVI (ne zazna 4 v vrsto)
    i = 1
    poteze = [-9, -10, -11, -1, 9, 10, 11]
    for pot in poteze:
        poz = pozicija
        while i <= 4:
            if i == 4:
                print("Čestitam, ", igralec, ". igralec je zmagal!")
                solved = True
                i += 1
                continue
            elif poz + pot not in land:
                break
            elif land[poz + pot] == igralec:
                i +=1
                poz += pot
            else:
                break
    igralec = igralec % 2 + 1
