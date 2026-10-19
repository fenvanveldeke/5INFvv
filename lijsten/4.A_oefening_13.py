zin = input("voer een zin in:")
woorden = zin.lower().split()

unieke_woorden =[]
#stap 1: unieke lijst maken met alle verschillende woorden
for woord in woorden:
    if woord not in unieke_woorden:
        unieke_woorden.append(woord)

#stap 2 : per uniek woord tellen hoe vaak het voorkomt
for uniek in unieke_woorden:
    teller = 0
    for woord in woorden:
        if woord == uniek:
            teller = teller + 1
    print(f"{uniek}:{teller} ")
