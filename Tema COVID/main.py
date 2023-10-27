import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definim URL-urile corespunzătoare fiecărei date
urls = [
    'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/',
    'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00/',
    'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00/',
    'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00/',
    'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/'
]

# Definim header-ul pentru DataFrame
header = ['NR. CRT', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03']

# Initializăm un DataFrame goală
df = pd.DataFrame(columns=header)

# Parcurgem fiecare URL și extragem datele
for i, url in enumerate(urls):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Gasim tabelul care contine datele dorite
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')

    # Extragem datele din fiecare rand al tabelului si le adaugam in DataFrame
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if len(cols) < len(header) - 1:
            cols += [''] * (len(header) - 1 - len(cols))
        new_row = [i + 1] + cols
        df = pd.concat([df, pd.DataFrame([new_row], columns=header)], ignore_index=True)

total_row = ['Total', ''] + [df[header[j]].sum() for j in range(2, len(header))]
df.loc[len(df.index)] = total_row
df.to_excel("date_covid.xlsx", index=False)
