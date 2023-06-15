from collections import Counter

utilizatori = [
    {
        'nume': 'George',
        'filme': ['Shrek', 'Bond', 'Fight Club']
    },
    {
        'nume': 'Cristian',
        'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
    },
    {
        'nume': 'Stefan',
        'filme': ['Fight Club', 'Slumdog Milionare']
    }
]

toateFilmele = [film for utilizator in utilizatori for film in utilizator['filme']]

numarFilme = Counter(toateFilmele)
celeMaiVizionate = numarFilme.most_common()

numeFilme = [film for film, _ in celeMaiVizionate]
print("Cel mai vizionat film: " + numeFilme[0])

numarUtilizatori = Counter()
for utilizator in utilizatori:
    numeUtilizator = utilizator['nume']
    numarFilmeVizionate = len(utilizator['filme'])
    numarUtilizatori[numeUtilizator] += numarFilmeVizionate

topUtilizatori = numarUtilizatori.most_common()
numeUtilizatori = [utilizator for utilizator, _ in topUtilizatori]
print("Utilizatorul cu cele mai multe filme vizionate: " + numeUtilizatori[0])

stringResult1 = ", ".join(numeFilme)
print("Top filme dupa vizionari: " + stringResult1)

stringResult2 = ", ".join(numeUtilizatori)
print("Top utilizatori cu cele mai multe filme vizionate: " + stringResult2)
