lijst = []
for getal in range(1,51):
    aantal_delers = 0
    for deler in range(1,getal+1):
        if getal % deler == 0:
        aantal_delers = aantal_delers

    if aantal_delers == 2:
    lijst.append(getal)
print(lijst)