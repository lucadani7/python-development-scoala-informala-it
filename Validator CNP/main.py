def esteAnBisect(an):
    return an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)


def verificaCNP(cnp):
    if len(cnp) != 13:
        return False
    sexCentury = int(cnp[0])
    year = int(cnp[1:3])
    # 1, 2, 7, 8, 9 pt persoane nascute intre 1900 si 1999 sau straini rezidenti in Romania
    if sexCentury in [1, 2, 7, 8, 9]:
        year += 1900
    # 3 si 4 pt persoanele nascute intre 1800 si 1899
    elif sexCentury in [3, 4]:
        year += 1800
    # 5 si 6 pt persoanele nascute intre 2000 si 2099
    elif sexCentury in [5, 6]:
        year += 2000
    month = int(cnp[3:5])
    if month < 1 or month > 12:  # verificam luna nasterii
        return False
    day = int(cnp[5:7])
    conditie1 = day < 1 or day > 31
    conditie2 = month == 2 and not esteAnBisect(year) and day > 28
    conditie3 = month == 2 and esteAnBisect(year) and day > 29
    conditie4 = day > 30 and month in [4, 6, 9, 11]
    if conditie1 or conditie2 or conditie3 or conditie4:
        return False
    countyCode = int(cnp[7:9])
    if countyCode < 1 or countyCode > 52:
        return False
    weights = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    controlSum = sum(int(cnp[i]) * weights[i] for i in range(len(weights)))
    controlDigit = 1 if controlSum % 11 == 10 else controlSum % 11
    if int(cnp[12]) != controlDigit:
        return False
    return True


cnp = "1980928440024"
result = "CNP-ul este valid." if verificaCNP(cnp) else "CNP-ul nu este valid."
print(result)
