import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook, '\n')
print(len(phonebook))

mydictionary{}

mydictionary = dict(m=8, n=9)

print()
print('*****  end section 1 ********')
print()

print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'chris'
if name in phonebook:
    print(f"Name: {name} Phone Number: {phonebook[name]}")
else:
    print(f"{name} is not in the phone book")


print()
print('*****  end section 2 ********')
print()

print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'

print(phonebook)

print()
print('*****  end section 3 ********')
print()

print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()

print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()
'''

for key in phonebook:
    print(f"Name: {key} Phone Number: {phonebook[key]}")

for values in phonebook.values():
    print(values)

for k,v in phonebook.items():                               # .items produces tuple (has parenthases)
    print(f"Name: {k} Phone Number: {v}")                   # having two varaibles k , v allows you to break up tuple and edit them

print()
print('*****  end section 5 ********')
print()
'''
print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('chris', 'Not Found')                  # second value is the default value if key is not found in dict
print(phone)

phonebook.clear()
print(phonebook)


print()
print('*****  end section 6 ********')
print()

print()
print('*****  start section 7 - using pop method ********')
print()


print(phonebook)
phone = phonebook.pop('Chris', 'name not found')
print(phone)
print(phonebook)


print()
print('*****  end section 7 ********')
print()

print()
print('*****  start section 8 - using popitem ********')
print()


phone = phonebook.popitem()
print(phone)

print(phonebook)



print()
print('*****  end section 8 ********')
print()
'''
print()
print('*****  start section 9 - using random and converting to list ********')
print()

# listofkeys = list(phonebook)
# print(listofkeys)

# randomkey = random.choice(listofkeys)
# print(randomkey)
# print(phonebook[randomkey])

print(phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()
