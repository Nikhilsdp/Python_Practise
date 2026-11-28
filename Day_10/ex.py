for i in range(11):
    print(i)
num = 0
while num<=10:
    print(num)
    num=num+1
for i in range(10,-1,-1):
    print(i)
num = 10
while num>=0:
    print(num)
    num=num-1

for i in range(1, 8):
    print("  " + "#" * i)
print("\n")
for i in range(1, 8):
    print("  " + "#" * 8)
print("\n")

for i in range(1,11):
    print(f'{i} x {i} = {i*i}')

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in lst:
    print(item)
for i in range(101):
    if i % 2 != 0:
        continue
    else:
        print(i)
for i in range(101):
    if i % 2 == 0:
        continue
    else:
        print(i)

total = 0
for i in range(101):
    total += i
print("The sum of all numbers is",total)

total_even = 0
total_odd = 0
for i in range(101):
    if i % 2 == 0:
        total_even += i
        
    else:
        total_odd += i
print(f"The sum of all evens is:{total_even}\nAnd the sum of all odds is{total_odd}")






