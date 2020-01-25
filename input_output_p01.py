# Read Text file - create list - read list & create dictionary
# Then use dictionary & create lambda expression to read and display output

dict1 = dict({})
list1 = []

with open("C:\\Users\\Johan Swan\\Downloads\\lambda-names.txt") as f:
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
