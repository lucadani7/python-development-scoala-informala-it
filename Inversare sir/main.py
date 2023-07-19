def inversare_sir():
    cuvant = input("Introduceti de la tastatura un cuvant: ")
    if len(cuvant) < 2:
        print("Ai introdus " + cuvant + ". Pe ecran se va afisa: ")
        print(cuvant)
        return
    caractere = []
    for elem in cuvant:
        caractere.insert(0, elem)
    cuvant_inversat = "".join(caractere)
    print("Cuvantul inversat al lui " + cuvant + " este " + cuvant_inversat)


inversare_sir()
