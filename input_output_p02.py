swan = open("C:\\Users\\Johan Swan\\Downloads\\stelliewalie.txt", 'tr')
for b in swan:
    print(b)
    if "PETRE" in b.upper():
        print('Yes')
    else:
        print('no')
    if 'kobie' in b.lower():
        print('Hallelujah')
    else:
        print('ag nee')

print()
print('--------------------------------------------------------------------------')
print()

def readDisplay():
    global line
    while line:
        print(line)
        line = sariemarais.readline()

with open("C:\\Users\\Johan Swan\\Downloads\\sariemarais.txt", 'r') as sariemarais:
    line = sariemarais.readline()
    readDisplay()

print()
print('--------------------------------------------------------------------------')
print()

with open("C:\\Users\\Johan Swan\\Downloads\\karaballa.txt", 'r') as garabaldi:
    lines = garabaldi.readline()
    while lines:
        for line in lines[::-1]:
            print(line, end='')
        lines = garabaldi.readline()

print()
print('--------------------------------------------------------------------------')
print()

cities = ["Johannesburg", "Melbourne", "Pretoria", "Sydney", "Danabaai", "Phalaborwa", "Edenton", "Tauranga",
          "Nelson Bays", "Standerton"]

person = {1: "Sanet & Doors", 2: "Amanda & Hennie", 3: "Chris en sy vreeslose vriendin",
           4: "Andries & Rentia", 5: "Pa, Ma, Ida & Johan", 6: "Richard Roekeloos en Erika",
           7: "Petra & Alden", 8: "Estelle & Johannes", 9: "Thomas, Natasha & Roxanne",
           10: "Julie & Gerrie"}

person_locat = 1
phrase1 = "   ---   lives in   ---    "

with open("C:\\Users\\Johan Swan\\Downloads\\cities.txt", 'w') as swannie_file:
    for city in cities:
        print(person[person_locat], phrase1, city.upper(), file=swannie_file)
        print('  ', file=swannie_file, flush=True)
        person_locat += 1

print()
print('--------------------------------------------------------------------------')
print()

with open("C:\\Users\\Johan Swan\\Downloads\\AAseBB.txt", 'r') as taranaki:
    lines = taranaki.readline()
    while lines:
        for line in lines[::-1]:
            print(line, end='')
        lines = taranaki.readline()
print()
print('--------------------------------------------------------------------------')
print()
