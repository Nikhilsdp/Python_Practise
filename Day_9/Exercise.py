"""age = int(input('Enter your age:'))
if age >= 18 :
    print('You are old enough to drive!')
else :
    print(f'You need {18-age} more years to drive!') """

my_age = 23
your_age = int(input("Enter your age:"))

if your_age > my_age:
    print(f'You are {your_age - my_age} years older than me.')
elif your_age < my_age:
    print(f'You are {my_age - your_age} years younger than me.')
else:
    print('Me and you are of same age.')
