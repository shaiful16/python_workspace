from itertools import chain
from collections import defaultdict

'''adding 2 dictionary'''
k0 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
k1 = {'bookC': 2, 'bookD': 4, 'bookE': 5}
z = dict(k0, **k1)
print(z)

dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
dict2 = {'bookC': 2, 'bookD': 4, 'bookE': 5}
dict3 = defaultdict(list)
for k, v in chain(dict1.items(), dict2.items()):
    dict3[k].append(v)
for k, v in dict3.items():
    print(k, v)


dict = {'Name': 'Zara', 'Age': 7, 'class': 'Manni'}
print("dict['Name']: ", dict['Name'], "dict['Age']: ", dict['Age'])
print()
for k, v in dict.items():
    print(k, v)
print()
