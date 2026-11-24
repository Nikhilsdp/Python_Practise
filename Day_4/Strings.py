sub_stirng1 = ['Thirty', 'Days', 'Of', 'Python']
sub_stirng2 = ['Coding', 'for', 'all']

single_string = ' '.join(sub_stirng1)
print(single_string)

print(' '.join(sub_stirng2))

company = "coding for all" 
print(company)
print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])

print(company.index('coding'))
print(company.find('coding'))

print(company.replace('coding', 'Python'))

print(company.split())

split_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(split_string.split(','))

print(company[0])
print(company[-1])
print(company[10])

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

print(sentence[31:54])

print(company.startswith('coding'))
print(company.endswith('coding'))

company1 = '  Coding for all  '
print(company1.strip())

list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' #'.join(list))

print("I am enjoying this challenge.\n I just wonder what is next.")

challenge = "Name\tAge\tCountry\tCity"
challenge1 = "Asabeneh\t25\tFinland\tHelsinki"
print(challenge.expandtabs(15))
print(challenge1.expandtabs(15))

radius = 10
area = 3.14 * radius ** 2
print(f'The area of the circle with radius {radius} is {area:.2f}')

a = 8
b = 6
print(f'8 + 6 = {a+b}')
print(f'8 - 6 = {a-b}')
print(f'8 * 6 = {a*b}')
print(f'8 / 6 = {(a/b):.2f}')
print(f'8 % 6 = {a%b}')
print(f'8 // 6 = {a//b}')
print(f'8 ** 6 = {a**b}')