a = 0
if a > 0:
    print('A is a positive number.')

elif a < 0:
    print('A is a negative number.')
else:
    print('A is zero')

b = 6
print('B is positive') if b > 0 else print('B is neagative')

     
user = 'James'
access_level = 5
if user == 'Admin' or access_level >= 4 :
    print('Access Granted!')
else :
    print('Access Denied!')
