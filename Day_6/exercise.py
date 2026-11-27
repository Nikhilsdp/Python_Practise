# Day 6 tuple exercises

# Level 1
empty_tuple = ()

brothers = ("Alex", "Sam")
sisters = ("Taylor", "Morgan")
siblings = brothers + sisters
print("Siblings:", siblings)
print("Number of siblings:", len(siblings))

father = "Jordan"
mother = "Casey"
family_members = siblings + (father, mother)
print("Family members:", family_members)

# Level 2
*siblings, father, mother = family_members
print("Unpacked siblings:", siblings)
print("Unpacked parents:", father, mother)

fruits = ("banana", "orange", "mango")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "eggs")
food_stuff_tp = fruits + vegetables + animal_products
print("Food tuple:", food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)

middle_start = (len(food_stuff_tp) - 1) // 2
print(middle_start)
middle_end = len(food_stuff_tp) // 2 + 1
print(middle_end)
print("Middle item(s):", food_stuff_tp[middle_start:middle_end])
print("First three foods:", food_stuff_lt[:3])
print("Last three foods:", food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Is Estonia a Nordic country?", "Estonia" in nordic_countries)
print("Is Iceland a Nordic country?", "Iceland" in nordic_countries)
