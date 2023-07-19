def verificare_paritate(valoare):
    return valoare % 2 == 0


while True:
    sir = input("Introduceti un numar de la tastatura: ")
    if sir.isnumeric():
        break
    print("Sirul pe care trebuie sa-l introduceti de la tastatura trebuie sa fie neaparat numar!")
valoare = int(sir)
mesaj = str(valoare) + " este par" if verificare_paritate(valoare) else str(valoare) + " este impar"
print(mesaj)
