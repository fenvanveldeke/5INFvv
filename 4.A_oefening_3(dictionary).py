telefoonboek = {}
afgesloten = False 
for beurt in range(1000):
    if not afgesloten:
        print("1.telefoonboek menu")
        print("2. contact zoeken")
        print("3.contact verwijderen")
        print("4 alle contacten weergeven")
        print("5. afsluiten")
        keuze = input("kies een optie:")
        print()

        if keuze == "1":
            naam = input("Naam: ")
            nummer = input("Telefoonnummer")
            telefoonboek[naam] = nummer
            print("contact toegevoegd")

        elif keuze == "2" :
            naam = input("welke naam zoek je ")
        if naam in telefoonboek:
            print(f"{naam}: {telefoonboek[naam]}")
        else:
            print("contact niet gevonden")
        
        if keuze == "3":
            naam = input("Welk contact wil je vewijderen?")
        if naam in telefoonboek:
            del telefoonboek[naam]
        else:
            print("contact niet gevonden")


        if keuze == "4":
            if len(telefoonboek) == 0:
                print("het is lelijk")
            else: 
                print("telefoonboek:")
                for naam,nummer in telefoonboek.items():
                    print(f"{naam}:{nummer}")
        elif keuze == "5": 
            print("tot ziens")
            afgesloten == True

        else:
            print("je hebt een ongeldige keuze ingegeven")