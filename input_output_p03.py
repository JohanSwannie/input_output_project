import xml.etree.ElementTree as jt

atree = jt.parse('jsfirst.xml')
aroot = atree.getroot()

print(aroot)
print(aroot.tag)                      # very first tag under root
print(aroot[0].tag)                   # 2nd tag
print(aroot[0].attrib)                # attributes of 2nd tag


for c in aroot[2][0:6]:
    print(c.text)

print('-' * 175)

for x in aroot[0]:
    print(x.tag, x.attrib, x.text)    # tags under 2nd tag with attributes and text

for x in aroot.findall('book'):       # print text for all records for author & title
    author = x.find('author').text
    title = x.find('title').text
    print(author, '   ---   ', title)

for x in aroot[0].iter('description'):   # change desription of complete file
    d = str(x.text)
    d = ''
    e = d + 'Hello Swannie'
    x.text = str(e)
    x.set('updated', 'yes')
atree.write('jsfunny.xml')

for x in aroot.iter('description'):   # change desription of complete file
    d = str(x.text) + 'Hello Stellie'
    x.text = str(d)
    x.set('updated', 'yes')
atree.write('js2nd.xml')

jt.SubElement(aroot[0], 'Newtagsnaggy') # add 4 new sub-tags for 1st 4 tags
jt.SubElement(aroot[1], 'Newtagsnaggy')
jt.SubElement(aroot[2], 'Newtagsnaggy')
jt.SubElement(aroot[3], 'Newtagsnaggy')

for x in aroot.iter('Newtagsnaggy'):        # iterate throug 4 new tags and add text
    y = "The greatest taste in Ginger Beer"
    x.text = str(y)
atree.write('js3rd.xml')

for x in aroot.iter('Newtagsnaggy'):        # iterate throug 4 new tags and print the content
    print(x.tag, x.attrib, x.text)

aroot[0][0].attrib.pop('name')               # delete attribute
aroot[0].remove(aroot[0][0])                 # remove 1st sub tag
aroot[1][1].clear()                          # clear 2nd sub tag title

from xml.dom import minidom as md
btree = md.parse('foodexample.xml')

#OR

# data = open('foodexample.xml')
# m = md.parse(data)

#OR

#m = md.parseString('<.....')

tagdesc = btree.getElementsByTagName('food')[0]
print(tagdesc)
print(tagdesc.attributes['name'].value)

tagdesc = btree.getElementsByTagName('food')
print(tagdesc[1].firstChild.data)

for x in tagdesc:
    print(x.secondChild.data)

print(len(tagdesc))
