word = "banananana"
i = word.find('na')   # idendx dinxa, where na will start first 
print(i)


counts = {'chuck': 1, "annie": 43, "jane": 100}
for key in counts:
    print(key)
    if counts[key] > 10:
        print(key, counts[key])

# annie 43
# jane 100

d = dict()
d ["quencey"] = 1
d["beau"] = 5
d["kris"] = 9

for k, i in d.items():
    print(k, i)

# quencey 1
# beau 5
# kris 9


lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
#[(100, 'jane'), (43, 'annie'), (1, 'chuck')]


# print(sorted([ (v, k)  for k, v in counts.items()], reverse=True )


# only white space characetr ( regex) =>    \s        ( small s for WHITEsPace)


import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)


#['csev@umich.edu', 'cwen@iupui.edu']



# Help improve or add subtitles.
# What is XSD?
# The W3C Schema specification for XML.


import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])


# How does the PageRank algorithm work?
# It determines which pages are most highly connected.