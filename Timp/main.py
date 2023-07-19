def conversie_timp():
    while True:
        valoare = input("Introduceti numarul de secunde de la tastatura: ")
        if not valoare.isnumeric():
            print("Numarul de secunde trebuie sa fie obligatoriu un numar: ")
            continue
        if int(valoare) < 0:
            print("Numarul de secunde trebuie sa fie obligatoriu un numar pozitiv:  ")
            continue
        if valoare.isnumeric() and int(valoare) >= 0:
            break
    nr_secunde = int(valoare)
    nr_minute = nr_secunde // 60
    nr_secunde_ramase = nr_secunde % 60
    nr_ore = nr_minute // 60
    nr_minute_ramase = nr_minute % 60
    print("In " + str(nr_secunde) + " secunde sunt: " + str(nr_ore) + " ore, " + str(
        nr_minute_ramase) + " minute si " + str(nr_secunde_ramase) + " secunde")


conversie_timp()
