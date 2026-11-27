# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')

it_companies.update(['SpaceX', 'Nvidia'])
print(len(it_companies))
it_companies.remove('IBM')
print(len(it_companies))
it_companies.discard('IBM')

print(A  | B)
print(A & B)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

st = set(age)
print(len(age) == len(st))

str = "I am a teacher and I love to inspire and teach people"
st1 = str.split(" ")
st2=set(st1)
print(st2)
print(len(st1))
print(len(st2))




