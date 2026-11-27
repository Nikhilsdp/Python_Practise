empty_dict = {}

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':23,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
print(person)
print(len(person))

print(person['first_name'])
print(person['age'])
#print(person['city']) ERROR
print(person.get('city')) 

person['city'] = 'Spain'
print(person)
print(person['city'])
person['skills'].append('AIML')
print(person)

person['age'] = 14
print(person)

print('address' in person)

dct1 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct1.pop('key1')
print(dct1)
dct1.popitem()
print(dct1)

del dct1['key3']
print(dct1)

dct2 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct2.items())
print(dct2.clear())

del dct2
#print(dct2)

dct_copy = dct.copy()
print(dct_copy)

print(dct.keys())
print(dct.values())
