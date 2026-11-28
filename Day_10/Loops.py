count = 0
while count < 5:
    print(count)
    count = count+1
else :
    print(count)

while count < 5:
    print(count)
    count = count+1
    if count == 3:
        break
count1 = 0
while count1 < 5:
    if count1 == 3:
        count1+=1
        continue
    print(count1)
    count1 = count1 + 1
numbers = [1,2,3,4,5,6]

for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print("\n",language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
for key, value in person.items():
    print(key,"=>", value)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
numbers = (0,1,2,3,4,5,6)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('The next number must be', number+1) if number !=5 else print("Loop's end.")
print('outside the loop')

lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)
lst2 = list(range(1,11,2))
print(lst2)
lst1 = list(range(11,-2,-1))
print(lst1)

for i in range(0,11,2):
    print(i)
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

for number in range(6):
    pass