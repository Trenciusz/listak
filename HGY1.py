gyumolcsok = []

while True:
    gyumolcs = input("Adjon meg egy gyümölcsöt, vagy írj be azt, hogy 'vége' a program befejezéséhez: ")
    if gyumolcs == 'vége':
        break
    if gyumolcs in gyumolcsok:
        print("Ezt a gyumolcsot már beírtad egyszer")
    else:
        gyumolcsok.append(gyumolcs)
    
print("A listázott gyümölcsök:")
for gyumolcs in reversed(gyumolcsok):
    print(gyumolcs, end=" ")