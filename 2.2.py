print("Írjon be kis 'a' betűvel kezdődő szavakt!")
print("Ha nem kis 'a' betűvel kezdődő szót ír be, az nem lesz tárolva!")
print("A végén ki fogom írni az összes tárolt szót!")

szavak = []

while True:
    szo = input("Írjon be egy szót: ")
    if szo == "":
        break
    if szo[0] == "a" or "A":
        szavak.append(szo)

print("Az eltárolt szavak: ")
for szo in szavak:
    print(szo)
