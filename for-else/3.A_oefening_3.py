import random
getal = random.randint(1, 10)
raad = int(input("geef een getal tussen 1 en 10"))
if getal == raad:
    print("goed gedaan")
else:
    print(f"fout het was {getal}")
