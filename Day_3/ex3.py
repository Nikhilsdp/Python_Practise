# Day 3: 30 days of Pyhton Programming 23-11-2026
print("___Area of triangle___")
base = float(input('Enter the base:'))
height = float(input('Enter the height:'))

area_tri = 0.5 * base * height
print("The arae of triangle is:",area_tri)

print("___Perimeter of triangle___")
a = float(input('Enter the side a:'))
b = float(input('Enter the side b:'))
c = float(input('Enter the side c:'))

perimeter = a + b + c
print("The perimeter of triangle is:",perimeter)


# Calculate slope, x-intercept and y-intercept

m = 2
c = -2

# Slope
slope = m

# X-intercept (put y = 0)
x_intercept = -c / m

# Y-intercept (put x = 0)
y_intercept = c

print("Slope =", slope)
print("X-intercept =", x_intercept)
print("Y-intercept =", y_intercept)

x1 = 2
y1 = 2
x2 = 6
y2 = 10
m1 = y2-y1 / x2 - x1
print('Slope m1=',m1)

x = int(input("Enter the value of x:"))
y = x**2 + 6*x + 9
print("The value of Y:", y) 

print('on' in 'Python' and 'on' in 'Dragon' )

print('jargon' in 'I hope this course is not full of jargon')
print(not('on' in 'Python' and 'on' in 'Dragon' ))
str = 'python'
print(len(str), float(len(str)), int(len(str))) 


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")



print(7//3 == int(2.7))

print(type('10') == type(10))

hrs = int(input("Enter the hours:"))
price = int(input("Enter the price per hours:"))
print ("Your weekly earning is:", hrs * price)

year = int(input("Enter number of years you have lived:"))
print("You have lived for", year * 31536000, "seconds.")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)