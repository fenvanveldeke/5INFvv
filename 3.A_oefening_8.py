aankoopbedrag = int(input("geef je bedrag:"))
if aankoopbedrag > 100:
    print("je krijgt 10%")
    print(f" {aankoopbedrag*10/100}")
if aankoopbedrag > 50 and aankoopbedrag <= 100:
    print("je krijgt 5%")
    print(f"{aankoopbedrag*5/100}")
else:
    print("helaas geen korting")

