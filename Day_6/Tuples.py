#Day 6 of 30 days of Python
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

tpl1 = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

print(len(tpl1))

print("First Item:", tpl1[0])
print(f'First Friut: {fruits[0]}\nSecond Friut: {fruits[1]}')
print(f'Second Last Friut: {fruits[-2]}\nLast Friut: {fruits[-1]}')

print("Tuple Slicing:")
print("All fruits:", fruits[0:])
print("All fruits:", fruits[-4:])
print("All fruits in reverse:", fruits[::-1])

tpl_mod = list(tpl1)
print(tpl_mod)

print('orange' in fruits)
print('apple' in fruits)

join_tpl = tpl1 + fruits
print(join_tpl)
del join_tpl




