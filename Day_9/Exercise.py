"""age = int(input('Enter your age:'))
if age >= 18 :
    print('You are old enough to drive!')
else :
    print(f'You need {18-age} more years to drive!') 

my_age = 23
your_age = int(input("Enter your age:"))

if your_age > my_age:
    print(f'You are {your_age - my_age} years older than me.')
elif your_age < my_age:
    print(f'You are {my_age - your_age} years younger than me.')
else:
    print('Me and you are of same age.')

marks = int(input("Enter your marks:"))
if marks >= 90 and marks <=100:
    print("Your grade is A")
elif marks >= 80 and marks <=89:
    print("Your grade is B")
elif marks >= 70 and marks <=79:
    print("Your grade is C")
elif marks >= 60 and marks <=69:
    print("Your grade is D")
elif marks >= 0 and marks <=59:
    print("Your grade is F")
else :
    print("Invalid range of marks!")

month = input("Enter the month:")
if month in ['September','October','November'] :
    print('The season is Autumn')
elif month in ['December', 'January','February']:
    print('The season is Winter')
elif month in ['March', 'April','May']:
    print('The season is Spring')
else:
    print('The season is Summer') 
fruits = ['banana', 'orange', 'mango', 'lemon']

u_friut = input('Enter the friut name:')

if u_friut in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(u_friut)
    print("The fruit is added to the list", fruits)
""" 
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    mid_skill = person['skills'][len(person['skills']) // 2]
    print(mid_skill)
    print('Python' in person['skills'])

    skills = set(person['skills'])
    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('He is a fullstack developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    else:
        print('unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


