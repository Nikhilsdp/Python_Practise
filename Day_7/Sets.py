st = set()
st = {'item1', 'item2', 'item3', 'item4'}

print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(type(fruits))
print(len(fruits))

print('Does set st contain item3?', 'item3' in st)

st.add('item5')
print(st)

fruits.add('cherry')
print(fruits)

st.update(['item6', 'item7'])
print(st)


vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

st.remove('item7')
print(st)


print(st.pop())
st.clear()

#del st
print(st)

friuts1 = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
friuts1 = set(friuts1)
print(friuts1)

print(fruits.union(friuts1))

st1 = {'item1', 'item2', 'item3', 'item4'}
print(st1 | fruits)

st2 = {'item3', 'item2'}
print(st1.intersection(st2))
print(st1&st2)

print(st2.issubset(st1))
print(st1.issuperset(st2))

print(st1.difference(st2))
print(st1-st2)


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

print(st1.isdisjoint(st2))

