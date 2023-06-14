def stergereTotiCareNuSuntMultipliiLuiTrei(lista):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] % 3 != 0:
            del lista[i]
    return lista


ourList = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
ourListSorted = ourList
ourListSortedDescending = ourList
print("Lista initiala: " + str(ourList))
ourListSorted.sort()
print("Lista sortata ascendent: " + str(ourListSorted))
ourListSortedDescending.sort(reverse=True)
print("Lista sortata descendent: " + str(ourListSortedDescending))
listEvenElem = ourListSorted
listEvenElem = sorted(listEvenElem[::2])
print("Lista cu elemente pare: " + str(listEvenElem))
listOddElem = ourListSorted
listOddElem = sorted(listOddElem[1::2])
print("Lista cu elemente impare: " + str(listOddElem))
listMultiplesOfThree = ourList
listMultiplesOfThree = sorted(stergereTotiCareNuSuntMultipliiLuiTrei(listMultiplesOfThree))
print("Lista cu multiplii lui 3: " + str(listMultiplesOfThree))
