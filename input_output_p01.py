# Read Text file - create list - read list & create dictionary
# Then use dictionary & create lambda expression to read and display output

# EXAMPLE 1 - READ 

dict1 = dict({})
list1 = []

with open("lambda-names.txt") as f:
    for line in f:
        list1.append(line.strip().split())
    f.close()

print(list1)

for x, y, z in sorted(list1):
    dict1[x] = y + ' ' + z

print(dict1)

full_name = lambda fn, ln_age: fn.strip().title() + '  ' + ln_age.strip().title()

for fn, ln in dict1.items():
    print(full_name(fn, ln))

# EXAMPLE 2 - READ

swan = open("stelliewalie.txt", 'tr')
for b in swan:
    print(b)
    if "PETRE" in b.upper():
        print('Yes Petre in file')
    else:
        print('Petre not in file')
    if 'kobie' in b.lower():
        print('kobie definitely in file')
    else:
        print('kobie not in file')

print()
print('--------------------------------------------------------------------------')
print()

# EXAMPLE 3 - READ

def readDisplay():
    global line
    while line:
        print(line)
        line = sariemarais.readline()

with open("sariemarais.txt", 'r') as sariemarais:
    line = sariemarais.readline()
    readDisplay()

print()
print('--------------------------------------------------------------------------')
print()

# EXAMPLE 4 - READ

with open("karaballa.txt", 'r') as garabaldi:
    lines = garabaldi.readline()
    while lines:
        for line in lines[::-1]:
            print(line, end='')
        lines = garabaldi.readline()

print()
print('--------------------------------------------------------------------------')
print()

# EXAMPLE 5 - READ

cities = ["Johannesburg", "Melbourne", "Pretoria", "Sydney", "Danabaai", "Phalaborwa", "Edenton", "Tauranga",
          "Nelson Bays", "Standerton"]

person = {1: "Sanet & Doors", 2: "Amanda & Hennie", 3: "Chris en sy vreeslose vriendin",
           4: "Andries & Rentia", 5: "Pa, Ma, Ida & Johan", 6: "Richard Roekeloos en Erika",
           7: "Petra & Alden", 8: "Estelle & Johannes", 9: "Thomas, Natasha & Roxanne",
           10: "Julie & Gerrie"}

person_locat = 1
phrase1 = "   ---   lives in   ---    "

with open("cities.txt", 'w') as swannie_file:
    for city in cities:
        print(person[person_locat], phrase1, city.upper(), file=swannie_file)
        print('  ', file=swannie_file, flush=True)
        person_locat += 1

print()
print('--------------------------------------------------------------------------')
print()

# EXAMPLE 6 - READ

with open("AAseBB.txt", 'r') as taranaki:
    lines = taranaki.readline()
    while lines:
        for line in lines[::-1]:
            print(line, end='')
        lines = taranaki.readline()
print()
print('--------------------------------------------------------------------------')
print()

# EXAMPLE 7 - WRITE

nbr = 1
list1 = ["Python", "Javascript", "JQuery", "JSON", "HTML", "CSS"]

with open("languages.txt", "w") as nf1:
    for langs in list1:
        # print(langs, file = nf1) # Will write file with records on each line
        nf1.write(str(nbr)+ ') '); nf1.write(langs); nf1.write('   '); nf1.write('\n')
        nbr += 1
        
# EXAMPLE 8 - APPEND

list2 = ["7) C#.Net   ", "8) Ruby   ", "9) Scala   ", "10) Hadoop   ", "11) Cobol   "]
with open("languages.txt", "a") as af1:
    for newlang in list2:
        af1.write(newlang); af1.write('\n')
    
# EXAMPLE 9 - DELETE

import os
os.remove("languages.txt")
