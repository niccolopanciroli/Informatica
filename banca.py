numeroscatti = int(input("Quale è il numero dei tuoi scatti? "))
prezzoscatto = int(input("Quale è il prezzo di un singolo scatto? "))
canonefisso = int(input("Quale è il tuo canone fisso? "))
prezzo= numeroscatti * prezzoscatto + canonefisso
print("Il prezzo della bolletta ammonta a: ", prezzo)


input()


tappa1 = int(input("Quanti km hai percorso per raggiungere la prima tappa? "))
tappa2 = int(input("Quanti km hai percorso per raggiungere la seconda tappa? "))
tappa3 = int(input("Quanti km hai percorso per raggiungere la terza tappa? "))
kmtotali= tappa1 + tappa2 + tappa3
print("I km totali percorsi sono:", kmtotali)
kmmiglio = kmtotali * 1.609
kmiarde = kmmiglio * 1760
print("Km in miglia= ", kmmiglio)
print("Km in iarde= ", kmiarde)