# O functie recursiva care cauta binar un element intr-o lista. Aici nu m-a interesat pozitia elementului in lista,
# ci doar am testat existenta sa in lista
def cautareBinara(lista, elem, st, dr):
    if st > dr:
        return False
    middle = (st + dr) // 2
    if lista[middle] == elem:
        return True
    elif lista[middle] > elem:
        return cautareBinara(lista, elem, st, middle - 1)
    return cautareBinara(lista, elem, middle + 1, dr)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# inainte de a cauta binar un element in lista b, trebuie sa sortam lista b, altfel ar fi trebuit sa fac cautare liniara
b.sort()
for elem in a:
    if cautareBinara(b, elem, 0, len(b) - 1):
        c.append(elem)  # daca un element din lista a exista si in lista b, il adaugam la lista c

c = list(set(c))  # eliminam eventualele duplicate
print(c)
