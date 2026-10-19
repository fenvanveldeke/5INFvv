cijfers = {
    "Nederlands": 7,
    "Engels": 6,
    "Wiskunde": 8,
    "Informatica": 9,
    "Geschiedenis": 5,
    "Aardrijkskunde": 7,
    "Biologie": 6
}

totale_som = 0
aantal_vakken = 0

for vak,cijfer in cijfers.items():
    totale_som = totale_som + cijfer
    aantal_vakken = aantal_vakken + 1

gemiddelde = totale_som / aantal_vakken
print("het gemiddeldecijfer is :", round(gemiddelde,1))

hoogste_cijfer = 0
hoogste_vak = ""

for vak,cijfer in cijfers.items():
    if hoogste_cijfer < cijfer:
        hoogste_cijfer = cijfer
        hoogste_vak = vak
print(f"het vak met hoogste cijfer :")
print(f"{hoogste_vak}:{hoogste_cijfer}")

laagste_cijfer = 10
laagste_vak = ""

for vak,cijfer in cijfers.items():
    if laagste_cijfer > cijfer:
        laagste_cijfer = cijfer
        laagste_vak = vak

print("het laagste cijfer is")
print(f"{laagste_vak}: {laagste_cijfer}")

print(f"vakken met een voldoende")
for vak,cijfer in cijfers.items():
    if cijfer >= 6:
        print(f"{vak}")




