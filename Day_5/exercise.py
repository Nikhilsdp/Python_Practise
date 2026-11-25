lst = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print(lst[0])
index1=len(lst)//2
print(lst[index1])

print(lst[-1])

mixed_data_types = ['nikhil', 23, 6.3]
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
print(len(it_companies))

print(it_companies[0])
print(it_companies[-1])
print(it_companies[len(it_companies)//2])

it_companies[0] = "FACEBOOK"
print(it_companies)
hash1 = ["#"]
it_companies_joined = it_companies + hash1
print(it_companies_joined)

print(it_companies.index('Google'))

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])
print(it_companies[-3:])

print(it_companies[len(it_companies)//2])

it_companies.pop(0)
print(it_companies)

pos = len(it_companies)//2
it_companies.pop(pos)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)
#del it_companies
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
print(full_stack)


full_stack.append('Python')
full_stack.append('Redux')

print(full_stack)









