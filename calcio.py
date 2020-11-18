portieri = ["donnarumma", "szczesny", "handanovic", "sirigu", "strakosha", "gollini", "pau lopez", "meret"]
difensori = ["romagnoli", "theo hernandez", "bonucci", "de ligt", "de vrij", "skriniar", "izzo", "nkoulou", "acerbi","luiz felipe", "hateboer", "gosens", "mancini", "kolarov","koulibaly","di lorenzo"]
centrocampisti = ["kessie", "bennacer", "pjanic", "dybala", "ericksen", "barella", "ansaldi", "baselli", "milinkovic-savic", "luis alberto", "papu gomez", "ilicic", "pellegrini", "veretout", "allan", "fabian ruiz"]
attaccanti = ["ibrahimovic", "ronaldo", "lukaku", "belotti", "immobile", "zapata", "dzeko", "mertens"]

formazione = []
corretto = 0
sbagliato = 0
giocate = 0

print(portieri)
por1 = input("scegli un portiere ")
formazione.append(por1)
portieri.remove(por1)

print(difensori)
dif1 = input("scegli un difensore ")
formazione.append(dif1)
difensori.remove(dif1)
print(difensori)
dif2 = input("scegli un difensore ")
formazione.append(dif2)
difensori.remove(dif2)
print(difensori)
dif3 = input("scegli un difensore ")
formazione.append(dif3)
difensori.remove(dif3)
print(difensori)
dif4 = input("scegli un difensore ")
formazione.append(dif4)
difensori.remove(dif4)

print(centrocampisti)
cen1 = input("scegli un centrocampista ")
formazione.append(cen1)
centrocampisti.remove(cen1)
print(centrocampisti)
cen2 = input("scegli un centrocampista ")
formazione.append(cen2)
centrocampisti.remove(cen2)
print(centrocampisti)
cen3 = input("scegli un centrocampista ")
formazione.append(cen3)
centrocampisti.remove(cen3)

print(attaccanti)
att1 = input("scegli un attaccante ")
formazione.append(att1)
attaccanti.remove(att1)
print(attaccanti)
att2 = input("scegli un attaccante ")
formazione.append(att2)
attaccanti.remove(att2)
print(attaccanti)
att3 = input("scegli un attaccante ")
formazione.append(att3)
attaccanti.remove(att3)

gk = [por1]
cb = [dif1, dif2, dif3, dif4]
cm = [cen1, cen2, cen3]
st = [att1, att2, att3]

input()

print(formazione)

input()

print("1.Portiere")
print("2.Difensore")
print("3.centrocampista")
print("4.attaccante")
scontro = input("cosa vuoi fare?" )

while True:
    while True:
        if scontro == "1":
            print(gk)
            gk1 = input("scegli un portiere ")
            if gk1 == "donnarumma":
                dif = 88
                con = 54
                att = 23
                gk.remove(gk1)
            elif gk1 == "szczesny":
                dif = 89
                con = 52
                att = 25
                gk.remove(gk1)
            elif gk1 == "handanovic":
                dif = 90
                con = 48
                att = 22
                gk.remove(gk1)
            elif gk1 == "sirigu":
                dif = 87
                con = 57
                att = 24
                gk.remove(gk1)
            elif gk1 == "strakosha":
                dif = 87
                con = 55
                att = 28
                gk.remove(gk1)
            elif gk1 == "gollini":
                dif = 85
                con = 47
                att = 31
                gk.remove(gk1)
            elif gk1 == "pau lopez":
                dif = 88
                con = 56
                att = 21
                gk.remove(gk1)
            elif gk1 == "meret":
                dif = 86
                con = 45
                att = 25
                gk.remove(gk1)
            
            print("1.Difesa")
            print("2.Controllo")
            print("3.Attacco")
            tattica = int(input("Cosa vuoi fare? "))

            if tattica == 1:
                print("la tua difesa")
                print(dif)
                gg = dif
            elif tattica == 2:
                print("il tuo controllo")
                print(con)
                gg = con
            elif tattica == 3:
                print("il tuo attacco")
                print(att)
                gg = att

            from random import randint
            numcasuale = randint(65,96)

            print("l'avvesario:")
            print(numcasuale)
        
            if gg > numcasuale:
                corretto = corretto + 1
                print("Complimenti hai segnato e sei",corretto, "a", sbagliato)
            elif gg == numcasuale:
                print("Clamoroso!Pareggio!")
            elif gg < numcasuale:
                sbagliato = sbagliato + 1
                print("Mi dispiace, hai subito gol...e sei", corretto, "a", sbagliato)

            giocate = giocate + 1

        if scontro == "2":
            for n in range(1,5):
                print(cb)
                cb1 = input("scegli un difensore ")
                #"romagnoli", "theo hernandez", "bonucci", "de ligt", "de vrij", "skriniar", "izzo", "nkoulou",
                #  "acerbi","luiz felipe", "hateboer", "gosens", "mancini", "kolarov","koulibaly","di lorenzo
                if cb1 == "romagnoli":
                    dif = 87
                    con = 66
                    att = 37
                    cb.remove(cb1)
                elif cb1 == "theo hernandez":
                    dif = 81
                    con = 83
                    att = 76
                    cb.remove(cb1)
                elif cb1 == "bonucci":
                    dif = 88
                    con = 74
                    att = 40
                    cb.remove(cb1)
                elif cb1 == "de ligt":
                    dif = 87
                    con = 65
                    att = 46
                    cb.remove(cb1)
                elif cb1 == "de vrij":
                    dif = 88
                    con = 68
                    att = 44
                    cb.remove(cb1)
                elif cb1 == "skriniar":
                    dif = 88
                    con = 63
                    att = 41
                    cb.remove(cb1)
                elif cb1 == "izzo":
                    dif = 86
                    con = 58
                    att = 35
                    cb.remove(cb1)
                elif cb1 == "nkoulou":
                    dif = 86
                    con = 59
                    att = 38
                    cb.remove(cb1)
                elif cb1 == "acerbi":
                    dif = 87
                    con = 68
                    att = 42
                    cb.remove(cb1)
                elif cb1 == "luiz felipe":
                    dif = 85
                    con = 61
                    att = 39
                    cb.remove(cb1)
                elif cb1 == "hateboer":
                    dif = 79
                    con = 81
                    att = 75
                    cb.remove(cb1)
                elif cb1 == "gosens":
                    dif = 77
                    con = 80
                    att = 78
                    cb.remove(cb1)
                elif cb1 == "mancini":
                    dif = 85
                    con = 64
                    att = 48
                    cb.remove(cb1)
                elif cb1 == "kolarov":
                    dif = 82
                    con = 85
                    att = 79
                    cb.remove(cb1)
                elif cb1 == "koulibaly":
                    dif = 89
                    con = 58
                    att = 36
                    cb.remove(cb1)
                elif cb1 == "di lorenzo":
                    dif = 82
                    con = 78
                    att = 72
                    cb.remove(cb1)
                
                print("1.Difesa")
                print("2.Controllo")
                print("3.Attacco")
                tattica = int(input("Cosa vuoi fare? "))

                if tattica == 1:
                    print("la tua difesa")
                    print(dif)
                    gg = dif
                elif tattica == 2:
                    print("il tuo controllo")
                    print(con)
                    gg = con
                elif tattica == 3:
                    print("il tuo attacco")
                    print(att)
                    gg = att
                else:
                    print("errore")

                from random import randint
                numcasuale = randint(65,95)

                print("l'avvesario:")
                print(numcasuale)

                if gg > numcasuale:
                    corretto = corretto + 1
                    print("Complimenti hai segnato e sei",corretto, "a", sbagliato)
                elif gg == numcasuale:
                    print("Clamoroso!Pareggio!")
                elif gg < numcasuale:
                    sbagliato = sbagliato +1
                    print("Mi dispiace, hai subito gol...e sei",corretto, "a", sbagliato)

            giocate = giocate + 4

        if scontro == "3":
            for n in range(1,4):
                print(cm)
                cm1 = input("scegli un centrocampista ")
                #"kessie", "bennacer", "pjanic", "dybala", "ericksen", "barella", "ansaldi", "baselli", "milinkovic-savic",
                #  "luis alberto", "papu gomez", "ilicic", "pellegrini", "veretout", "allan", "fabian ruiz"
                if cm1 == "kessie":
                    dif = 83
                    con = 79
                    att = 75
                    cm.remove(cm1)
                elif cm1 == "bennacer":
                    dif = 79
                    con = 81
                    att = 70
                    cm.remove(cm1)
                elif cm1 == "pjanic":
                    dif = 77
                    con = 88
                    att = 78
                    cm.remove(cm1)
                elif cm1 == "dybala":
                    dif = 53
                    con = 88
                    att = 85
                    cm.remove(cm1)
                elif cm1 == "ericksen":
                    dif = 68
                    con = 90
                    att = 81
                    cm.remove(cm1)
                elif cm1 == "barella":
                    dif = 78
                    con = 83
                    att = 79
                    cm.remove(cm1)           
                elif cm1 == "ansaldi":
                    dif = 80
                    con = 80
                    att = 77
                    cm.remove(cm1)           
                elif cm1 == "baselli":
                    dif = 76
                    con = 82
                    att = 77
                    cm.remove(cm1)           
                elif cm1 == "milinkovic-savic":
                    dif = 76
                    con = 85
                    att = 79
                    cm.remove(cm1)
                elif cm1 == "luis alberto":
                    dif = 58
                    con = 87
                    att = 83
                    cm.remove(cm1)            
                elif cm1 == "papu gomez":
                    dif = 55
                    con = 88
                    att = 82
                    cm.remove(cm1)
                elif cm1 == "ilicic":
                    dif = 56
                    con = 86
                    att = 84
                    cm.remove(cm1)
                elif cm1 == "pellegrini":
                    dif = 75
                    con = 83
                    att = 77
                    cm.remove(cm1)
                elif cm1 == "veretout":
                    dif = 78
                    con = 84
                    att = 74
                    cm.remove(cm1)           
                elif cm1 == "allan":
                    dif = 84
                    con = 83
                    att = 70
                    cm.remove(cm1)
                elif cm1 == "fabian ruiz":
                    dif = 65
                    con = 86
                    att = 80
                    cm.remove(cm1)
                
                print("1.Difesa")
                print("2.Controllo")
                print("3.Attacco")
                tattica = int(input("Cosa vuoi fare? "))

                if tattica == 1:
                    print("la tua difesa")
                    print(dif)
                    gg = dif
                elif tattica == 2:
                    print("il tuo controllo")
                    print(con)
                    gg = con
                elif tattica == 3:
                    print("il tuo attacco")
                    print(att)
                    gg = att

                from random import randint
                numcasuale = randint(65,95)

                print("l'avvesario:")
                print(numcasuale)

                if gg > numcasuale:
                    corretto = corretto + 1
                    print("Complimenti hai segnato e sei",corretto, "a", sbagliato)
                elif gg == numcasuale:
                    print("Clamoroso!Pareggio!")
                elif gg < numcasuale:
                    sbagliato = sbagliato +1
                    print("Mi dispiace, hai subito gol...e sei",corretto, "a", sbagliato)

            giocate = giocate + 3

        if scontro == "4":
            for n in range(1,4):
                print(st)
                st1 = input("Scegli un attaccante ")
                #"ibrahimovic", "ronaldo", "lukaku", "belotti", "immobile", "zapata", "dzeko", "mertens"
                if st1 == "ibrahimovic":
                    dif = 34
                    con = 78
                    att = 89
                    st.remove(st1)
                elif st1 == "ronaldo":
                    dif = 36
                    con = 83
                    att = 93
                    st.remove(st1)
                elif st1 == "lukaku":
                    dif = 41
                    con = 75
                    att = 88
                    st.remove(st1)
                elif st1 == "belotti":
                    dif = 27
                    con = 77
                    att = 85
                    st.remove(st1)
                elif st1 == "immobile":
                    dif = 33
                    con = 79
                    att = 88
                    st.remove(st1)
                elif st1 == "zapata":
                    dif = 35
                    con = 74
                    att = 87
                    st.remove(st1)
                elif st1 == "dzeko":
                    dif = 27
                    con = 78
                    att = 87
                    st.remove(st1)
                elif st1 == "mertens":
                    dif = 30
                    con = 87
                    att = 86
                    st.remove(st1)
                
                print("1.Difesa")
                print("2.Controllo")
                print("3.Attacco")
                tattica = int(input("Cosa vuoi fare? "))

                if tattica == 1:
                    print("la tua difesa")
                    print(dif)
                    gg = dif
                elif tattica == 2:
                    print("il tuo controllo")
                    print(con)
                    gg = con
                elif tattica == 3:
                    print("il tuo attacco")
                    print(att)
                    gg = att

                from random import randint
                numcasuale = randint(65,95)

                print("l'avvesario:")
                print(numcasuale)

                if gg > numcasuale:
                    corretto = corretto + 1
                    print("Complimenti hai segnato e sei",corretto, "a", sbagliato)
                elif gg == numcasuale:
                    print("Clamoroso!Pareggio!")
                elif gg < numcasuale:
                    sbagliato = sbagliato +1
                    print("Mi dispiace, hai subito gol...e sei",corretto, "a", sbagliato)

            giocate = giocate + 3
            
        if giocate == 11:
            print("Gioco concluso")
            print("Risultato partita:")
            print(corretto, "-", sbagliato)
            break

        print("1.Portiere")
        print("2.Difensore")
        print("3.centrocampista")
        print("4.attaccante")
        scontro = input("cosa vuoi fare? ")
 
    restart = input("Vuoi rigiocare?")
    if restart == "no":
        break