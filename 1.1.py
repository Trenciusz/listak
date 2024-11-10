mondat = input("Adjon meg egy mondatot egy mondatvégi írásjellel: ")
irasjel = mondat[-1]

if irasjel == '?':
    print("Ez egy kérdő mondat")
elif irasjel == '.':
    print("Ez egy kijelentő mondat")
elif irasjel == '!':
    print("Ez a mondat vagy felkiáltó vagy óhajtó vagy felszólíó")
else:
    print("Nem adtál meg mondatvégi írásjelet")